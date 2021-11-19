FROM registry.access.redhat.com/ubi8/ubi:8.1

ENV description = ""

LABEL maintainer="timbuchinger@gmail.com"
LABEL description="$DESCRIPTION"

ADD entrypoint.sh /bin/entrypoint
RUN dnf -y install python3 git
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install ansible ansible-lint
RUN ansible-galaxy collection install google.cloud

COPY ansible.cfg /etc/ansible/ansible.cfg
COPY inventory.ini /etc/ansible/inventory.ini

WORKDIR /data
ENTRYPOINT ["ansible-lint"]
CMD ["--version"]