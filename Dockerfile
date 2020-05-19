FROM python:3.7-alpine
RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN pip install terraenv