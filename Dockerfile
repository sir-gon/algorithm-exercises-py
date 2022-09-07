FROM python:3.10.7-alpine3.16 as base

ENV WORKDIR=/app
WORKDIR ${WORKDIR}

FROM base as development

RUN apk add --update --no-cache make

FROM development as builder

COPY ./src ${WORKDIR}/src
COPY ./requirements.txt ${WORKDIR}/
COPY ./Makefile ${WORKDIR}/

RUN pip install -r requirements.txt

FROM builder as testing

WORKDIR /app

RUN ls -alh

CMD ["make", "all"]
