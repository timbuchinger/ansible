FROM registry.access.redhat.com/ubi8/ubi:8.1

ENV description = ""

LABEL maintainer="timbuchinger@gmail.com"
LABEL description="$DESCRIPTION"

ADD entrypoint.sh /bin/entrypoint
RUN yum install

COPY ansible.cfg /etc/ansible/ansible.cfg
COPY inventory.ini /etc/ansible/inventory.ini

ENTRYPOINT ["entrypoint"]
CMD ["ansible-runner", "run", "/runner"]