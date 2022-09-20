.MAIN: test
.PHONY: all clean dependencies help list test

help: list

list:
	@LC_ALL=C $(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

install: dependencies

dependencies:
	pip3 install --user -r requirements.txt

update:
	pip3 freeze > requirements.txt

upgrade:
	pip3 install --upgrade -r requirements.txt

lint: dependencies
	python3 -m pylint --verbose --recursive yes src/

test: dependencies
	pytest --verbose -o log_cli=true --log-cli-level=INFO src/

test/debug: dependencies
	pytest --verbose -o log_cli=true --log-cli-level=DEBUG --full-trace src/

test/bruteforce: dependencies
	BRUTEFORCE=true pytest --verbose -o log_cli=true --log-cli-level=DEBUG --full-trace src/

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


all: lint coverage
