from __future__ import (absolute_import, division, print_function)

from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

from ansible.plugins.callback import CallbackBase
from ansible.module_utils.common.text.converters import to_native
from ansible.errors import AnsibleError

from datetime import datetime
import os

DOCUMENTATION = '''
    callback: prometheus_callback_plugin
    type: notification
    short_description: Callback to send stats to a Prometheus push gateway.
    description:
      - Reports play run statistics to a Prometheus push gateway.
      - Specify the gateway URL in the environment variable GATEWAY_URL.
    requirements:
      - prometheus_client library
    '''


class CallbackModule(CallbackBase):

    '''
    Callback to send stats to a Prometheus push gateway.
    '''

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'prometheus_callback_plugin'

    def __init__(self, *args, **kwargs):
        super(CallbackModule, self).__init__()

    def v2_playbook_on_start(self, playbook):
        self.playbook = playbook
        print(playbook.__dict__)

    def v2_playbook_on_play_start(self, play):
        self.play = play
        self.gateway_url = os.environ['GATEWAY_URL']
        self.registry = CollectorRegistry()
        self.play_start_time = datetime.now()

    def v2_runner_on_ok(self, result):
        print('Successful task: Sending to gateway')

        diff = datetime.now() - self.play_start_time
        elapsed_time = int((diff.seconds * 1000) + (diff.microseconds / 1000))

        try:
            registry = CollectorRegistry()
            g = Gauge('play_last_success_seconds',
                      'Duration of the last successful play',
                      registry=registry)
            g.set(elapsed_time)
            push_to_gateway(self.gateway_url, job='batchA', registry=registry)
        except Exception as e:
            raise AnsibleError(
                'An error occurred: %s' % to_native(e))

        pass

    def v2_runner_on_failed(self, result, ignore_errors=False):
        print('Failed task: Sending to gateway')

        diff = datetime.now() - self.play_start_time
        elapsed_time = int((diff.seconds * 1000) + (diff.microseconds / 1000))

        try:
            registry = CollectorRegistry()
            g = Gauge('play_last_failure_seconds',
                      'Duration of the last failed play',
                      registry=registry)
            g.set(elapsed_time)
            push_to_gateway(self.gateway_url, job='batchA', registry=registry)
        except Exception as e:
            raise AnsibleError(
                'An error occurred: %s' % to_native(e))

        pass

    def v2_playbook_on_stats(self, stats):
        pass
