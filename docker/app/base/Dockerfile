FROM ubuntu:14.04
MAINTAINER Chris McKinnel <chris.mckinnel@tangentsnowball.com>

ENV HOME /root

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq              && \
    apt-get dist-upgrade -y         && \
    apt-get install -y build-essential \
                       libpq-dev       \
                       python-dev      \
                       python-pip      \
                       supervisor      \
                       uwsgi           \
                       memcached
RUN apt-get clean && apt-get autoclean

RUN easy_install -U pip

ADD docker/app/shared/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
