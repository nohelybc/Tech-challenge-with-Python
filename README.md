# Tech challenge with Python

## Description

The goal for this challenge is to write a Python code that flattens an array (list) of integers or lists of integers (which can be nested arbitrarily) to a flat array of integers.

For example, we have the following list:

```
[1, [2, [3, [4, 5]]]]
```

And our code need to return the following output:

```
[1, 2, 3, 4, 5]
```

## Implementation

- A function to iterate through the lists was created and lives in the file **main.py**
  - Recusivity principles were implemented to achieve iterate through several nested lists
  - A try/except statement was implemented to catch any kind of errors that could arise
  - _logging_ was imported to print the message with the exception in case of error
- Unit tests to verify the function is work properly were implemented and are in the path **test/test_main.py**
  - _unittest_ library was used to do the corresponding unit tests

## Result

You can try run the script by yourself [using the link of the project in repl.it](https://replit.com/@NohelyBadillo/Tech-Challenge). The unit tests are also included in the repl.it project.
