[![Python CI](https://github.com/sir-gon/projecteuler-py/actions/workflows/python.yml/badge.svg)](https://github.com/sir-gon/projecteuler-py/actions/workflows/python.yml) [![codecov](https://codecov.io/gh/sir-gon/projecteuler-py/branch/main/graph/badge.svg?token=U3N3HSC3YC)](https://codecov.io/gh/sir-gon/projecteuler-py) [![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fsir-gon%2Fprojecteuler-py.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fsir-gon%2Fprojecteuler-py?ref=badge_shield) [![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/6404/badge)](https://bestpractices.coreinfrastructure.org/projects/6404)

![GitHub](https://img.shields.io/github/license/sir-gon/projecteuler-py) ![GitHub language count](https://img.shields.io/github/languages/count/sir-gon/projecteuler-py) ![GitHub top language](https://img.shields.io/github/languages/top/sir-gon/projecteuler-py) [![Total alerts](https://img.shields.io/lgtm/alerts/g/sir-gon/projecteuler-py.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/sir-gon/projecteuler-py/alerts/)

# What is this?

[Project Euler](https://projecteuler.net/) provide some algorithms and mathematical problems to solve to be used as experience tests.

Use this answers to learn some tip and tricks for algorithms tests.

## Why I publish solutions?

As Project Euler says:

https://projecteuler.net/about#publish


```
I learned so much solving problem XXX, so is it okay to publish my solution elsewhere?
It appears that you have answered your own question. There is nothing quite like that "Aha!" moment when you finally beat a problem which you have been working on for some time. It is often through the best of intentions in wishing to share our insights so that others can enjoy that moment too. Sadly, that will rarely be the case for your readers. Real learning is an active process and seeing how it is done is a long way from experiencing that epiphany of discovery. Please do not deny others what you have so richly valued yourself.

However, the rule about sharing solutions outside of Project Euler does not apply to the first one-hundred problems, as long as any discussion clearly aims to instruct methods, not just provide answers, and does not directly threaten to undermine the enjoyment of solving later problems. Problems 1 to 100 provide a wealth of helpful introductory teaching material and if you are able to respect our requirements, then we give permission for those problems and their solutions to be discussed elsewhere.
```


If you have better answers or optimal solutions, fork and PR-me

Enjoy 😁 !


# Using Python 3 native runtime

## Requirements

You must install dependencies:

```
pip3 install -r requirements.txt
```

Or using make

```
make dependencies
```

## Testing silently

Every problem is a function with unit test.
Unit test has test cases and input data to solve the problem.

Run all tests:

```
pytest --verbose -o log_cli=true --log-cli-level=INFO --full-trace src/
```

### Testing with full logs

Run all tests with debug outputs:

```
pytest --verbose -o log_cli=true --log-cli-level=DEBUG --full-trace src/
```

## Testing using make

```
make test
```

### Enable all large BRUTEFORCE tests

Direct in host using a make:

```
make test -e BRUTEFORCE=true
```

### Enable all DEBUG outputs


```
make test -e LOG_LEVEL=debug
```

### Enable all large BRUTEFORCE tests and all DEBUG outputs

```
make test -e LOG_LEVEL=debug -e BRUTEFORCE=true
```

# Running with Docker 🐳

## Build a complete image with and run all tests
Running container with testing (final) target.

Designed to store all application files and dependencies as a complete runnable image.
Coverage results will be stored in host **/coverage** directory (mounted as volume).

```
# Build a complete image
docker-compose build projecteuler-py
docker-compose run --rm projecteuler-py make test coverage
```

## Enable BRUTEFORCE tests with full DEBUG output

With docker-compose:

```
docker-compose --profile testing run --rm projecteuler-py make test -e LOG_LEVEL=debug -e BRUTEFORCE=true
```

Using make:
```
make docker/compose-run -e LOG_LEVEL=DEBUG -e BRUTEFORCE=true
```

## Build and run a development image

Running container with development target.
Designed to develop on top of this image. All source application is mounted as a volume in **/app** directory.
Dependencies should be installed to run (not present in this target) so, you must install dependencies before run (or after a dependency add/change).

```
# install dependencies using docker runtime and store them in host directory
docker-compose build projecteuler-py-dev
docker-compose run --rm projecteuler-py-dev make dependencies
docker-compose run --rm projecteuler-py-dev make test

```

# About development

Developed with runtime:

```
python3 --version
Python 3.11.0
```

## Minimal dependencies

Third party libraries for CI/CD pipeline and TDD cycle (not used in runtime):

```
pip3 install coverage pylint pytest
```

## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fsir-gon%2Fprojecteuler-py.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fsir-gon%2Fprojecteuler-py?ref=badge_large)

## Coverage

[![Coverage](https://codecov.io/gh/sir-gon/algorithm-exercises-py/branch/main/graphs/tree.svg?token=VMH4I0MDFR)](https://app.codecov.io/gh/sir-gon/algorithm-exercises-py)

