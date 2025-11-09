ARG BASE_IMAGE="docker.io/python:3-alpine"
FROM $BASE_IMAGE

ARG REVEALJS_VERSION=5.2.1
ARG REVEALJS_SOURCE_ZIP=https://github.com/hakimel/reveal.js/archive/${REVEALJS_VERSION}.zip
RUN wget $REVEALJS_SOURCE_ZIP -O - | unzip -- -

WORKDIR /reveal.js-${REVEALJS_VERSION}
CMD python3 -m http.server
