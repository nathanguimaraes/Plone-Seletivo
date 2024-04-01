# syntax=docker/dockerfile:1
FROM varnish:7.4

LABEL maintainer="Nathan Guimaraes <nathan.guimaraez@gmail.com>" \
      org.label-schema.name="ploneutfpr-varnish" \
      org.label-schema.description="PloneUTFPR Varnish image." \
      org.label-schema.vendor="Nathan Guimaraes"

COPY etc/varnish.vcl /etc/varnish/default.vcl
