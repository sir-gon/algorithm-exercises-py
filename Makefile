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

mdlint:
	markdownlint '**/*.md' --ignore node_modules && echo '✔  Your code looks good.'

lint: test/static mdlint

test/static: dependencies
	python3 -m pylint --verbose --recursive yes src/
	python3 -m flake8 --verbose
	python3 -m pyright --verbose

test: env dependencies
	python3 -m pytest --verbose -o log_cli=true --log-cli-level=$(LOG_LEVEL) --full-trace src/

coverage: dependencies
	python3 -m coverage run -m pytest --verbose src/
	python3 -m coverage lcov -o coverage/lcov.info
	python3 -m coverage report

coverage/html: coverage
	python3 -m coverage html

outdated:
	pip3 list --outdated

update:
	pip3 freeze > requirements.txt

upgrade:
	pip3 list --outdated | cut -f1 -d' ' | tr " " "\n" | awk '{if(NR>=3)print}' | cut -d' ' -f1 | xargs -n1 pip3 install -U

clean:
	pip3 freeze > unins ; pip3 uninstall -y -r unins ; rm unins
	rm -f .coverage
	rm -fr .pytest_cache
	rm -fr htmlcov
	rm -fr coverage
	find . -path "*/*.pyc" -delete -print
	find . -path "*/*.pyo" -delete -print
	find . -path "*/__pycache__" -type d -print -exec rm -fr {} ';'

compose/build: env
	docker-compose --profile testing build

compose/rebuild: env
	docker-compose --profile lint build --no-cache
	docker-compose --profile testing build --no-cache

compose/mdlint: env
	docker-compose --profile lint build
	docker-compose --profile lint run --rm algorithm-exercises-py-mdlint make mdlint

compose/test/static: compose/build
	docker-compose --profile testing run --rm algorithm-exercises-py make test/static

compose/lint: compose/test/static compose/mdlint

compose/run: compose/build
	docker-compose --profile testing run --rm algorithm-exercises-py make test

all: lint coverage
