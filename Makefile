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


.MAIN: test
.PHONY: all clean dependencies help list test
.EXPORT_ALL_VARIABLES: # (2)

RUNTIME_TOOL=python3
PACKAGE_TOOL=pip3

# DOCKER
BUILDKIT_PROGRESS=plain
DOCKER_COMPOSE=docker compose

help: list
	@echo ""
	@echo "Note: create and activate the environment in your local shell type (example):"
	@echo "   python3 -m venv ./.venv"
	@echo "   source .venv/bin/activate"
	@echo "See: "
	@echo "   https://docs.python.org/3/library/venv.html#creating-virtual-environments"
	@echo "   https://docs.python.org/3/library/venv.html#how-venvs-work"

list:
	@LC_ALL=C $(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

env:
	@echo "################################################################################"
	@echo "## Environment: ################################################################"
	@echo "################################################################################"
	@printenv | grep -E "LOG_LEVEL|BRUTEFORCE|BUILDKIT_PROGRESS"
	@echo ""
	@echo "################################################################################"
	@echo "## Runtime: ####################################################################"
	@echo "################################################################################"
	@which $(PACKAGE_TOOL)
	@which $(RUNTIME_TOOL)
	@echo ""

install: dependencies

## Dependency management
dependencies:
	@echo "################################################################################"
	@echo "## Dependencies: ###############################################################"
	@echo "################################################################################"
	${PACKAGE_TOOL} install -r requirements.txt
	@echo "################################################################################"

outdated:
	${PACKAGE_TOOL} list --outdated

update:
	${PACKAGE_TOOL} freeze > requirements.txt

upgrade:
	${PACKAGE_TOOL} list --outdated | cut -f1 -d' ' | tr " " "\n" | awk '{if(NR>=3)print}' | cut -d' ' -f1 | xargs -n1 pip3 install -U

clean:
	${PACKAGE_TOOL} freeze > unins ; ${PACKAGE_TOOL} uninstall -y -r unins ; rm unins
	rm -f .coverage
	rm -fr .pytest_cache
	rm -fr htmlcov
	rm -fr coverage
	rm -fr build
	find . -path "*/*.pyc" -delete -print || true
	find . -path "*/*.pyo" -delete -print || true
	find . -path "*/__pycache__" -type d -print -exec rm -fr {} ';' || true

## Building process
build: env
	rsync -av --prune-empty-dirs \
  --exclude '*_test.py' \
  --exclude '*.pyc' \
  --exclude '.venv' \
  --exclude '__pycache__' \
  src/ build/

## Source code linting and formatting
lint/json:
	prettier --check ./src/**/*.json

lint/markdown:
	markdownlint '**/*.md' --ignore node_modules && echo '✔  Your code looks good.'

lint/yaml:
	yamllint --stric . && echo '✔  Your code looks good.'

lint: lint/markdown lint/yaml lint/json test/styling test/static

format/json:
	prettier --write ./src/**/*.json

format/sources:
	${RUNTIME_TOOL} -m autopep8 --in-place --recursive --aggressive --aggressive --verbose src/

format: format/sources format/json

## Static code analysis
test/static: dependencies
	${RUNTIME_TOOL} -m pylint --verbose --recursive yes src/
	${RUNTIME_TOOL} -m flake8 --verbose src/
	${RUNTIME_TOOL} -m pyright --verbose src/

test/styling: dependencies
	${RUNTIME_TOOL} -m pycodestyle --statistics src/
	${RUNTIME_TOOL} -m autopep8  --diff --recursive --exit-code --verbose .

## Unit tests and coverage
test: env dependencies
	${RUNTIME_TOOL} -m coverage run -m \
		pytest --verbose \
		-o log_cli=true \
		--log-cli-level=${LOG_LEVEL} \
		--full-trace src/
	${RUNTIME_TOOL} -m coverage report

coverage: test
	${RUNTIME_TOOL} -m coverage lcov -o coverage/lcov.info

coverage/html: test
	${RUNTIME_TOOL} -m coverage html
	open htmlcov/index.html

## Docker Compose commands
compose/build: env
	${DOCKER_COMPOSE} --profile lint build
	${DOCKER_COMPOSE} --profile testing build
	${DOCKER_COMPOSE} --profile production build

compose/rebuild: env
	${DOCKER_COMPOSE} --profile lint build --no-cache
	${DOCKER_COMPOSE} --profile testing build --no-cache
	${DOCKER_COMPOSE} --profile production build --no-cache

compose/lint/markdown: compose/build
	${DOCKER_COMPOSE} --profile lint run --rm algorithm-exercises-py-lint make lint/markdown

compose/lint/yaml: compose/build
	${DOCKER_COMPOSE} --profile lint run --rm algorithm-exercises-py-lint make lint/yaml

compose/test/styling: compose/build
	${DOCKER_COMPOSE} --profile lint run --rm algorithm-exercises-py-lint make test/styling

compose/test/static: compose/build
	${DOCKER_COMPOSE} --profile lint run --rm algorithm-exercises-py-lint make test/static

compose/lint: compose/lint/markdown compose/lint/yaml compose/test/styling compose/test/static

compose/test: compose/build
	${DOCKER_COMPOSE} --profile testing run --rm algorithm-exercises-py-test make test

compose/run: compose/build
	${DOCKER_COMPOSE} --profile production run --rm algorithm-exercises-py make run

all: lint coverage

run:
	ls -alh
