FROM rockylinux/rockylinux:9
MAINTAINER NXLog Ltd <operations@nxlog.org>

ENV NXLOG_VERSION=3.2.2329_rhel9.x86_64.rpm

LABEL name="nxlog-ce" \
      maintainer="operations@nxlog.org" \
      vendor="NXLog Ltd" \
      version=${NXLOG_VERSION} \
      release="1" \
      summary="nxlog is a modular, multi-threaded, high-performance log management solution" \
      description="nxlog is a modular, multi-threaded, high-performance log management solution"

USER root

# Set the working directory to /opt
WORKDIR /opt

# Add nxlog package
ADD nxlog-ce-*.rpm /opt/

# system update
RUN yum update -y && yum install -y epel-release

# install nxlog and available dependencies
RUN yum install -y nxlog-*.rpm && mkdir -p /run/nxlog && chown nxlog /run/nxlog

# yum and workdir cleanup
RUN yum clean all && \
rm -rf /var/cache/yum && \
rm -f /opt/nxlog-*.rpm

# Start nxlog
USER nxlog
ENTRYPOINT [ "/usr/bin/nxlog", "-f" ]
CMD [ "-c", "/etc/nxlog/nxlog.conf" ]
