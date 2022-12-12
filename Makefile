## REFERENCES:
## (1) Passing environment variable with fallback value to Makefile:
##    https://stackoverflow.com/a/70772707/6366150
## (2) Export environment variables inside "make environment"
##		https://stackoverflow.com/a/49524393/6366150
## (3) Uppercase to lowercase and vice versa
##		https://community.unix.com/t/uppercase-to-lowercase-and-vice-versa/285278/6
## (4) How do I trim leading and trailing whitespace from each line of some output?
## 		https://unix.stackexchange.com/a/279222/233927
## (5) Pytest log levels:
##		https://docs.pytest.org/en/latest/how-to/logging.html
############################################################################

## (1) ## Allowed values: info | warn | error | debug
LOG_LEVEL ?= info
## (3) (4)
LOG_LEVEL :=$(shell echo '${LOG_LEVEL}'| tr '[:lower:]' '[:upper:]'| tr -d '[:blank:]')

## (1) ## Allowed values: true | false
BRUTEFORCE ?= false
## (3) (4)
BRUTEFORCE :=$(shell echo '${BRUTEFORCE}'| tr '[:lower:]' '[:upper:]'| tr -d '[:blank:]')

# DOCKER
BUILDKIT_PROGRESS=plain

.MAIN: test
.PHONY: all clean dependencies help list test
.EXPORT_ALL_VARIABLES: # (2)

help: list

list:
	@LC_ALL=C $(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

env:
	@echo "################################################################################"
	@echo "## Environment: ################################################################"
	@echo "################################################################################"
	@printenv | grep -E "LOG_LEVEL|BRUTEFORCE|BUILDKIT_PROGRESS"
	@echo "################################################################################"

install: dependencies

dependencies:
	@echo "################################################################################"
	@echo "## Dependencies: ###############################################################"
	@echo "################################################################################"
	pip3 install --user -r requirements.txt
	@echo "################################################################################"
update:
	pip3 freeze > requirements.txt

upgrade:
	pip3 install --upgrade -r requirements.txt

lint: dependencies
	python3 -m pylint --verbose --recursive yes src/

test: env dependencies
	pytest --verbose -o log_cli=true --log-cli-level=$(LOG_LEVEL) --full-trace src/

coverage: dependencies
	coverage run -m pytest --verbose src/
	coverage report

coverage/html: coverage
	coverage html

clean:
	pip3 freeze > unins ; pip3 uninstall -y -r unins ; rm unins
	rm .coverage
	rm -fr .pytest_cache
	rm -fr htmlcov
	find . -path "*/*.pyc" -delete -print
	find . -path "*/*.pyo" -delete -print
	find . -path "*/__pycache__" -type d -print -exec rm -r {} ';'

docker/compose-build: env
	docker-compose --profile testing build

docker/compose-rebuild: env
	docker-compose --profile testing build --no-cache

docker/compose-run: docker/build
	docker-compose --profile testing run --rm projecteuler-py make test

all: lint coverage
