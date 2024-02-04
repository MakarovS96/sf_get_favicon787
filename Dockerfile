FROM alpine:latest
WORKDIR /opt/python/
RUN apk add python3 && apk add py3-requests
COPY src/get_favicon.py /opt/python/
ENTRYPOINT ["/usr/bin/python", "get_favicon.py"]
CMD ["www.yandex.ru"]