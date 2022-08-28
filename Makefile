.MAIN: test
.PHONY: all clean dependencies help list test

help: list

list:
	@LC_ALL=C $(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

dependencies:
	pip3 install -r requirements.txt

# upgrade:
#   pip3 install --upgrade -r requirements.txt

test: dependencies
	python3 -m unittest discover -s src -p '*_test.py'

clean:
	pip3 freeze > unins ; pip3 uninstall -y -r unins ; rm unins

all: test coverage
