FROM python:3.11.2-alpine3.16 as base

ENV WORKDIR=/app
WORKDIR ${WORKDIR}

FROM base as development

RUN apk add --update --no-cache make

FROM development as builder

COPY ./src ${WORKDIR}/src
COPY ./requirements.txt ${WORKDIR}/
COPY ./Makefile ${WORKDIR}/
RUN ls -alh

RUN pip install -r requirements.txt

FROM builder as testing

ENV LOG_LEVEL=INFO
ENV BRUTEFORCE=false

RUN adduser -D worker
RUN mkdir -p /app
RUN chown worker:worker /app

WORKDIR /app

COPY ./.pylintrc ${WORKDIR}/
COPY ./.coveragerc ${WORKDIR}/
RUN ls -alh

USER worker
CMD ["make", "test", "-e", "{DEBUG}"]
