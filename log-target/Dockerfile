# log-target/Dockerfile
FROM alpine:latest

# Asenna socat + python
RUN apk add --no-cache socat python3

# Luo logihakemisto
RUN mkdir -p /logs && touch /logs/received.log

WORKDIR /app

# Kopioi web-viewer
COPY server.py index.html ./

EXPOSE 5140 7777

# Käynnistä molemmat:
# 1) socat vastaanottaa ja kirjoittaa tiedostoon
# 2) python tarjoaa web UI:n
CMD sh -c "\
  socat TCP-LISTEN:5140,reuseaddr,fork SYSTEM:'tee -a /logs/received.log' & \
  python3 server.py \
"
