# API Testing with Python using Pytest and Request module

## Project is written using 

* Python v3.9.6
* Pytest v7.1.2

## Setup

Install all the required Python modules using `pip`:

You can get a copy of all files used in this tutorial by cloning this repository!

```shell
https://github.com/Milena1993/API_Python.git
```

## Using Python  with Pytest and Request moduce

### Install pytest
```shell
pip install pytest
```
### Install request module

```shell
pip install requests
```
### To generate random data import
```shell
from uuid import uuid4
```
### Assertions are done importing
```shell
from assertpy.assertpy import assert_that
```
### The assertpy library is available via PyPI. Just install with:

```
pip install assertpy
```

Run tests using: 
```shell
 python -m pytest -v tests/test_assertions.py
```
Run tests including all the print statments using:
```shell
 python -m pytest -v tests/test_assertions.py
```
Run tests in parallel using first install 
```shell
pip install pytest-xdist
```
and run using 
```shell
 python -m pytest -v tests/test_assertions.py
```
