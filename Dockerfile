###############################################################################
FROM python:3.12.4-alpine3.20 AS init

ENV WORKDIR=/app
WORKDIR ${WORKDIR}

RUN apk add --update --no-cache make

###############################################################################
FROM init AS base

ENV WORKDIR=/app
WORKDIR ${WORKDIR}

COPY ./Makefile ${WORKDIR}/
COPY ./requirements.txt ${WORKDIR}/
RUN make dependencies

###############################################################################
FROM base AS lint

ENV WORKDIR=/app
WORKDIR ${WORKDIR}

RUN apk add --update --no-cache make nodejs npm
RUN apk add --update --no-cache yamllint

RUN npm install -g --ignore-scripts markdownlint-cli

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
COPY ./src/ ${WORKDIR}/src
COPY ./requirements.txt ${WORKDIR}/
COPY ./setup.cfg ${WORKDIR}/
COPY ./Makefile ${WORKDIR}/

# code linting conf
COPY ./.pylintrc ${WORKDIR}/
COPY ./.coveragerc ${WORKDIR}/
COPY ./setup.cfg ${WORKDIR}/

# markdownlint conf
COPY ./.markdownlint.yaml ${WORKDIR}/

# yamllint conf
COPY ./.yamllint ${WORKDIR}/
COPY ./.yamlignore ${WORKDIR}/

CMD ["make", "lint"]

###############################################################################
FROM base AS development

COPY ./Makefile ${WORKDIR}/
COPY ./setup.cfg ${WORKDIR}/
COPY ./src/ ${WORKDIR}/src

RUN ls -alh

# CMD []

###############################################################################
FROM development AS builder

ENV WORKDIR=/app
WORKDIR ${WORKDIR}

RUN apk add --update --no-cache rsync

RUN rsync -av --prune-empty-dirs \
  --exclude '*_test.py' \
  --exclude '*.pyc' \
  --exclude '.venv' \
  --exclude '__pycache__' \
  src/ build/

# CMD []

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
COPY ./setup.cfg ${WORKDIR}/

RUN ls -alh

CMD ["make", "test"]

###############################################################################
### In production stage
## in the production phase, "good practices" such as
## WORKDIR and USER are maintained
##
FROM init AS production

ENV LOG_LEVEL=INFO
ENV BRUTEFORCE=false
ENV WORKDIR=/app
WORKDIR ${WORKDIR}

RUN adduser -D worker
RUN mkdir -p /app
RUN chown worker:worker /app

COPY ./Makefile ${WORKDIR}/

COPY --from=builder /app/build/ ${WORKDIR}/

RUN ls -alh

USER worker
CMD ["make", "run"]

# checkov:skip= CKV_DOCKER_2: production image isn't a service process (yet)
