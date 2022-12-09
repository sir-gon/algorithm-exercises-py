## REFERENCES:
## (1) Passing environment variable with fallback value to Makefile:
##    https://stackoverflow.com/a/70772707/6366150
##

DEBUG := "INFO" ## (1) ## INFO | DEBUG
BRUTEFORCE := "false" # true | false

.MAIN: test
.PHONY: all clean dependencies help list test

help: list

list:
	@LC_ALL=C $(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

env:
	@echo "################################################################################"
	@echo "## Environment: ################################################################"
	@echo "################################################################################"
	@printenv
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
	BRUTEFORCE=$(BRUTEFORCE) pytest --verbose -o log_cli=true --log-cli-level=$(DEBUG) --full-trace src/

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

docker/build:
	BUILDKIT_PROGRESS=plain docker-compose --profile testing build

docker/rebuild:
	BUILDKIT_PROGRESS=plain docker-compose --profile testing build --no-cache

docker/compose-run: docker/build
	docker-compose --profile testing run --rm projecteuler-py make test -e DEBUG=$(DEBUG) -e BRUTEFORCE=$(BRUTEFORCE)

all: lint coverage
