#!/bin/sh
FROM alpine:3.7

ENV BUILD_PACKAGES postgresql-dev build-base git pkgconfig \
python3-dev libxml2-dev jpeg-dev libressl-dev libffi-dev libxslt-dev py3-lxml \
postgresql-client poppler-utils antiword vim

ENV CAPACITA_VERSION=1.0.0-19 \
    CAPACITA_URL=https://github.com/interlegis/capacita.git

RUN rm -rf /var/cache/apk/* && \
    rm -rf /tmp/*

RUN apk --update add fontconfig && fc-cache -fv

RUN apk add --no-cache python3 tzdata && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache && \
    rm -f /etc/nginx/conf.d/*

RUN apk update --update-cache

RUN mkdir -p /var/interlegis && \
    apk add --update --no-cache $BUILD_PACKAGES


RUN cd /tmp \
 && git clone ${CAPACITA_URL} --depth=1 --branch ${CAPACITA_VERSION} \
 && mv /tmp/capacita /var/interlegis 

WORKDIR /var/interlegis/capacita/

RUN pip3 install -r /var/interlegis/capacita/requirements.txt --upgrade setuptools && \
    rm -r /root/.cache

# Configura timezone para BRT
# RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && echo "America/Sao_Paulo" > /etc/timezone

# manage.py bower install bug: https://github.com/nvbn/django-bower/issues/51

# compilescss - Precompile all occurrences of your SASS/SCSS files for the whole project into css files


# Remove .env(fake) e capacita.db da imagem
RUN rm -rf /var/interlegis/capacita/capacita/.env && \
    rm -rf /var/interlegis/capacita/capacita.db

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

RUN mkdir /var/log/capacita/ && \
    cd /var/interlegis/capacita

WORKDIR /var/interlegis/capacita/

# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]

CMD ["/var/interlegis/capacita/start.sh"]