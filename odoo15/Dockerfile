FROM odoo:15.0
MAINTAINER Ramy <hadjahmedrami@gmail.com>

COPY ./extra-addons  /mnt/extra-addons
USER root
RUN set -x; \
         pip3 install -r /mnt/extra-addons/requirements.txt \
         && rm -rf /root/.cache/pip/*  \
         && rm -rf /var/lib/apt/lists/*
         
USER odoo
