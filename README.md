# Project Euler

## Some solutions to the problems from Project Euler.

Quick solutions to some of the Project Euler problems (https://projecteuler.net/).
Implementation in C++, Python, Java (coming), C# (coming) for practicing.

**C++ solutions** are accompanied with googletest framework to practice unit-test driven development
and are documented in Doxygen style.

**Python solutions** are checked with PyUnit (unittest), and
include automated parsing of provided XML-file with the answers to the Euler problems.
Py-files are documented with Docstring.

## C++ Setup
- Set path to 'googletest' lib as `GOOGLE_TEST_PATH` environment variable (see *makefile*).

## C++ Compile & Test
```
make cppTest
```
## Python Setup
- Change the standard Python 3 interpreter alias if necessary (default is *py3*, see *makefile*).

## Python Compile & Test
```
make pyTest
```
