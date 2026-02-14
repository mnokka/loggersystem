# log-target/Dockerfile
FROM alpine:latest

# Asenna socat ja tarvittavat paketit
RUN apk add --no-cache socat

# Luo kansio ja tyhjä logitiedosto
RUN mkdir -p /logs && touch /logs/received.log

WORKDIR /logs

# Käytetään pipeä ja tee:ä, jotta socat ei kaadu tiedostoon
CMD ["sh", "-c", "socat TCP-LISTEN:5140,reuseaddr,fork SYSTEM:'tee -a /logs/received.log'"]