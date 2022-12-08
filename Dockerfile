FROM python:3.11.1-alpine3.16 as base

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

ENV DEBUG=INFO
ENV BRUTEFORCE=false

WORKDIR /app

COPY ./.pylintrc ${WORKDIR}/
COPY ./.coveragerc ${WORKDIR}/
RUN ls -alh

CMD ["make", "test", "-e", "{DEBUG}"]
