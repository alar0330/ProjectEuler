# Project Euler

## Some solutions to the problems from Project Euler.

Quick solutions to some of the Project Euler problems (https://projecteuler.net/).
Implementation in Python, Java, and C++.

**C++ solutions** are accompanied with unit tests within googletest for practicing with the framework. Inline documentation in *Doxygen* style.

**Python solutions** are cross-checked with PyUnit (unittest), and
include automated parsing of provided XML-file with the answers to the Euler problems.
Py-files are Docstring documented in *reST* style (*Sphinx*-compliant).

## C++ Setup
- Set the path to 'googletest' lib as `GOOGLE_TEST_PATH` environment variable (see *makefile*).

## C++ Compile & Test
```
make cppTest
```
## Python Setup
- Change the standard Python 3 interpreter alias if necessary (default is ```python```, see *makefile*).

## Python Compile & Test
```
make pyTest
```
