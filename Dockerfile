FROM python:3.12.2-alpine3.19 AS base

ENV WORKDIR=/app
WORKDIR ${WORKDIR}

FROM node:20.2.0-alpine3.16 AS lint

ENV WORKDIR=/app
WORKDIR ${WORKDIR}

COPY ./src ${WORKDIR}/src
RUN apk add --update --no-cache make
RUN npm install -g --ignore-scripts markdownlint-cli

RUN apk add --update --no-cache nodejs npm
RUN npm install -g --ignore-scripts pyright

FROM base AS development

RUN apk add --update --no-cache make

FROM development AS builder

COPY ./src ${WORKDIR}/src
COPY ./requirements.txt ${WORKDIR}/
COPY ./Makefile ${WORKDIR}/
COPY ./setup.cfg ${WORKDIR}/
RUN ls -alh

RUN pip install -r requirements.txt

### In testing stage, can't use USER, due permissions issue
## in github actions environment:
##
## https://docs.github.com/en/actions/creating-actions/dockerfile-support-for-github-actions
##
FROM builder AS testing

ENV LOG_LEVEL=INFO
ENV BRUTEFORCE=false

WORKDIR /app

COPY ./.pylintrc ${WORKDIR}/
COPY ./.coveragerc ${WORKDIR}/
RUN ls -alh

CMD ["make", "test", "-e", "{DEBUG}"]

### In production stage
## in the production phase, "good practices" such as
## WORKSPACE and USER are maintained
##
FROM builder AS production

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
