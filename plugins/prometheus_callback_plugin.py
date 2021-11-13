from __future__ import (absolute_import, division, print_function)
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

from ansible.plugins.callback import CallbackBase
from ansible import constants as C


from __main__ import cli
from datetime import datetime
import os
__metaclass__ = type

DOCUMENTATION = '''
    Sends playbook metrics to a Prometheus push gateway.
    '''


class CallbackModule(CallbackBase):
    '''
    Pushes metrics to Prometheus push gateway.
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
        self.gateway_url = os.environ['GATEWAY_URL'] # localhost:9091
        self.registry = CollectorRegistry()
        self.play_start_time = datetime.now()

    def v2_runner_on_ok(self, result):
        print('Successful task: Sending to gateway')

        play_end_time = datetime.now()

        elapsed_time = 0
        diff = play_end_time - self.play_start_time
        elapsed_time = int((diff.seconds * 1000) + (diff.microseconds / 1000))

        # TODO: send success metric

        pass

    def v2_runner_on_failed(self, result, ignore_errors=False):
        print('Failed task: Sending to gateway')

        play_end_time = datetime.now()

        elapsed_time = 0
        diff = play_end_time - self.play_start_time 
        elapsed_time = int((diff.seconds * 1000) + (diff.microseconds / 1000))

        # TODO: send failed metric

        pass

    def v2_playbook_on_stats(self, stats):
        pass
