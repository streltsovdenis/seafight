FROM python:3.8
LABEL maintainer="Denis Streltsov <dsv.streltsov@gmail.com>"

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/

ENTRYPOINT ["python", "app.py"]