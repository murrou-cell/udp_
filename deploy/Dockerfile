FROM alpine:3.15

# This hack is widely applied to avoid python printing issues in docker containers.
# See: https://github.com/Docker-Hub-frolvlad/docker-alpine-python3/pull/13
ENV PYTHONUNBUFFERED=1

RUN echo "**** install Python ****" && \
    apk add --no-cache python3 && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    \
    echo "**** install pip ****" && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi

# RUN apk add --no-cache openrc
# RUN apk add --no-cache openssh
# RUN echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
# RUN rc-update add sshd
# #RUN rc-service sshd start
# RUN passwd -u root

RUN apk add --no-cache git
RUN git clone https://github.com/murrou-cell/udp_.git

# RUN apk add --no-cache openrc     
# RUN rc-update add local default
# RUN cp udp_/init_scripts/start_udp.start /etc/local.d/
# RUN chmod 755 /etc/local.d/start_udp.start

EXPOSE 51820/udp
EXPOSE 8881/udp 
EXPOSE 51820/tcp
EXPOSE 8881/tcp
EXPOSE 22/tcp

ENTRYPOINT cd udp_ && python3 client.py --DEST_IP 20.223.235.86

