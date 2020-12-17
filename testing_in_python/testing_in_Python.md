## Quick intro to Python `assert`

- You can write both integration tests and unit tests in Python
- Tests in Python are based on conditional logic; we are checking the output of some function or process against a known (expected) output
- For a unit test in Python, we use the `assert` command
  For example, here's how we would test if an input is of the correct datatype

```
input = ['x', 'y', 'z']

assert type(input) == 'list', 'Should be a list'
```

this wouldn't return any output because our test passes
Breakdown the code:

- `assert` to state that we want to test a specific process
- `type(input) == 'list` is our conditional logic
  - if this line of code evaluates to true, our test passes
- `, 'Should be a list'` is our custom `AssertionError` message
  - if our test fails, this message will be shown in the output

If we ran the same test with a failing input

```
input = 'list'

assert type(input) == 'list', 'Should be a list'
```

We would raise an assertion error and be provided with our custom message

```
...
AssertionError: Should be a list
```

## test runners

- if we ask google what a test runner is, we get: "Test runner is the execution unit of the incovation flow. This is where the tests actually run".
  - Hmm... a little vague
- A test runner is the library or tool that picks up an assembly (or a source code directory) that contains unit tests and settings, executes them, and writes tehe test results to either the console or log files
- there are a myriad of test runners available for Python
- some examples of testing libraries

  - `unittest` -- built into Python
  - `nose`/`nose2`
  - `pry`
  - `pytest` -- our choice for today

- test runners, sometimes referred to as _testing frameworks_, typically hook into your test's assertions so that they can provide information when an assertion fails.
- `uninttest`, for example, provides a number of helpful out-of-the-box assertion utilities
  - the downside to frameworks like `unittest` is that even a small set of tests requires a fair amount of boilerplate code.
- for example, if we simply wanted to make sure framework was functioning properly, we could write two tests: one that always passes, and one that always fails.
  To do this using `unittest`, we'd need the following code:

```
# file name test_using_unitest.py
from unittest import TestCase

class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)
```

We would then execute the tests with the following `unittest` command

```
python -m unittest discover
```

Which would give us our expected one pass, one fail result

```
FAIL: test_always_fails (test_with_unittest.TryTesting)
------------------------------------------------------------
Traceback (most recent call last):
  File "/.../test_with_unittest.py", line 9, in test_always_fails
    self.assertTrue(False)
AssertionError: False is not True

------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```
