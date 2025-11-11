ARG BASE_IMAGE="docker.io/caddy:2-alpine"
FROM $BASE_IMAGE

ARG REVEALJS_VERSION=5.2.1
ARG REVEALJS_SOURCE_ZIP=https://github.com/hakimel/reveal.js/archive/${REVEALJS_VERSION}.zip
ARG HIGHLIGHTJS_VERSION=10.7.3
ARG HIGHLIGHTJS_SOURCE=https://cdnjs.cloudflare.com/ajax/libs/highlight.js/${HIGHLIGHTJS_VERSION}/highlight.min.js
RUN wget "$REVEALJS_SOURCE_ZIP" -O - | unzip -d / -- - \
    && wget "$HIGHLIGHTJS_SOURCE" -O "/reveal.js-${REVEALJS_VERSION}/highlight.min.js" \
    && printf ":80 {\n  root *  /reveal.js-${REVEALJS_VERSION}\n  header Access-Control-Allow-Origin \"*\"\n file_server\n}\n" > /etc/caddy/Caddyfile

WORKDIR /reveal.js-${REVEALJS_VERSION}
