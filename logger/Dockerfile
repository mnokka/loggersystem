FROM alpine:3.19

RUN apk add --no-cache bash

WORKDIR /app

COPY generate.sh /app/generate.sh
RUN chmod +x /app/generate.sh

CMD ["/app/generate.sh"]
