###############################################################################
FROM python:3.12.4-alpine3.20 AS base

ENV WORKDIR=/app
WORKDIR ${WORKDIR}

###############################################################################
FROM base AS lint

ENV WORKDIR=/app
WORKDIR ${WORKDIR}

RUN apk add --update --no-cache make nodejs npm
RUN apk add --update --no-cache yamllint

RUN npm install -g --ignore-scripts markdownlint-cli
RUN npm install -g --ignore-scripts pyright

# [!TIP] Use a bind-mount to "/app" to override following "copys"
# for lint and test against "current" sources in this stage

# YAML sources
COPY ./.github ${WORKDIR}/
COPY ./compose.yaml ${WORKDIR}/

# Markdown sources
COPY ./docs ${WORKDIR}/
COPY ./README.md ${WORKDIR}/
COPY ./LICENSE.md ${WORKDIR}/
COPY ./CODE_OF_CONDUCT.md ${WORKDIR}/

# Code source
COPY ./src ${WORKDIR}/
COPY ./requirements.txt ${WORKDIR}/
COPY ./setup.cfg ${WORKDIR}/
COPY ./Makefile ${WORKDIR}/

# markdownlint conf
COPY ./.markdownlint.yaml ${WORKDIR}/

# yamllint conf
COPY ./.yamllint ${WORKDIR}/
COPY ./.yamlignore ${WORKDIR}/

# pylint and covergae
COPY ./.pylintrc ${WORKDIR}/
COPY ./.coveragerc ${WORKDIR}/

CMD ["make", "lint"]

###############################################################################
FROM base AS development

RUN apk add --update --no-cache make

###############################################################################
FROM development AS builder

COPY ./src ${WORKDIR}/src
COPY ./requirements.txt ${WORKDIR}/
COPY ./Makefile ${WORKDIR}/
COPY ./setup.cfg ${WORKDIR}/
RUN ls -alh

RUN pip install -r requirements.txt

###############################################################################
### In testing stage, can't use USER, due permissions issue
## in github actions environment:
##
## https://docs.github.com/en/actions/creating-actions/dockerfile-support-for-github-actions
##
FROM builder AS testing

ENV LOG_LEVEL=INFO
ENV BRUTEFORCE=false

WORKDIR /app

COPY ./.coveragerc ${WORKDIR}/
RUN ls -alh

CMD ["make", "test", "-e", "{DEBUG}"]

###############################################################################
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

RUN ls -alh

USER worker
CMD ["make", "test", "-e", "{DEBUG}"]
