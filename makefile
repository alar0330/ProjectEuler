# OpenMP-bench: makefile
#

# Googletest settings
GTEST_PATH = ${GOOGLE_TEST_PATH}
GTEST_LIB = gtest
GTEST_FLAGS = -L$(GTEST_PATH) -l$(GTEST_LIB) -lpthread

# C++ settings
C++ = g++
WFLAGS = -Wall -pedantic
OFLAGS =

# Python settings
PY3 = py3

# Directory settings
out = out
bin = bin

# Phonies
.PHONY = cppUnit cppTest pyTest clean

	
# C++: Compile & Run
cppTest: cppUnit
	$(bin)/testRunner.exe

cppUnit: testRunner.cpp
	$(C++) $(WFLAGS) $(GTEST_FLAGS) -o $(bin)/testRunner.exe $<

	
# Python: Compile & Run
pyTest:
	$(PY3) testRunner.py

	
# Clean up
clean:
	del *.exe $(out)/*.o *.out
