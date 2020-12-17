## What is pytest/ why pytest

- `pytest` is a test runner for Python
- `pytest` has been one of the most popular Python testing frameworks for many years running
- a 'plugin-based' feature-rich ecosystem for testing Python code
- it's functionality is designed with ease-of-use and productivity in mind
- quite a bit less boilerplate code required compared to other Python test runners
- super robust and easy to get started with
  - can run existing tests out of the box
    - includes functionality for reading tests written with `unittest`

## General

Most functional tests follow the Arrange-Act-Assert model:

1. **Arrange**, or set up, the conditions for the test
2. **Act** by calling some function or method
3. **Assert** that some end condition is true

going back to our one passing, one failing example, in `pytest` it's as simple as

```
def always_pass():
    assert True
def always_fail():
    assert False
```

Our arrange and act are all taken care of for us, no need to import any libraries or use any classes. We don't even need to call our testing functions! All we do to run our tests now, is enter the pytest command in the command line:

```
$ pytest
```

#### Install

with pip:

```
python -m pip install pytest
```

- `pytest` command now available from command line

#### writing some tests

#### evaluating test results

- if you've used `unittest` before, `pytest` output might look a little foreign
- `pytest` reporst show
  1. system state, including which version of Python, pytest and pluggins you have installed
  2. `rootdir`, or the directory `pytest` is searching for configurations and tests
  3. the number of tests the runner discovered
  4. output then indicates the status of each test
     - A dot (`.`) means that the test passed
     - An F means the test has failed
       - for tests that fail, the report gives a detailed breakdown of where the failure occured (will highlight which line of code contained the logic that caused the test to fail)
     - An E means the test raised an unexpected exception (script non-Assertion error)
