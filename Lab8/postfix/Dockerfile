FROM alpine:latest

RUN apk add --no-cache postfix bash mailx

COPY main.cf /etc/postfix/main.cf

RUN touch /var/log/mail.log

CMD ["sh", "-c", "postfix start-fg"]
