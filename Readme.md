!WIP!

[![Tests](https://github.com/adamlaszlo91/tdd-chip-8-python/actions/workflows/workflow.yml/badge.svg?branch=main)](https://github.com/adamlaszlo91/tdd-chip-8-python/actions/workflows/workflow.yml)
[![Coverage](https://codecov.io/gh/adamlaszlo91/tdd-chip-8-python/branch/main/graph/badge.svg)](https://codecov.io/gh/adamlaszlo91/tdd-chip-8-python)

# tdd-chip-8-python
An exercise in TDD by writing a CHIP-8 interpreter.

## Features

##  Requirements
- Python 3.14

## Usage
### Install dependencies
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Start game

## Test
```
coverage run --branch -m pytest
coverage report --show-missing
```
or
```
sh test.sh
```

## Acknowledgments

This project used 
[Cowgod's Chip-8 Technical Reference v1.0](http://devernay.free.fr/hacks/chip8/C8TECH10.HTM). Thank you.