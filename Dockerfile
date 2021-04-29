FROM python:3.8-slim

ARG uid=1000

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends -y graphviz make wget \
 && useradd -d /home/user -m -s /bin/bash -u $uid user \
 && wget -qq https://github.com/rust-lang/mdBook/releases/download/v0.4.7/mdbook-v0.4.7-x86_64-unknown-linux-gnu.tar.gz -O - | tar -xzf - -C /usr/bin/

USER $uid

WORKDIR /usr/src
