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
