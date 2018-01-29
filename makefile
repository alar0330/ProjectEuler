###########################
# ---- PROJECT EULER ---- #
###########################



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
test = test
lib = lib

# TestRunner
trun = testRunner

# Phonies
.PHONY = cppUnit cppTest pyTest clean

	
# C++: Compile & Run
cppTest: cppUnit
	@ $(bin)/$(trun).exe

cppUnit: $(out)/$(trun).o
	$(C++) $^ $(GTEST_FLAGS) -o $(bin)/$(trun).exe
	
$(out)/$(trun).o: $(test)/$(trun).cpp
	$(C++) -c $< $(WFLAGS) -o $@
	
	
# Python: Compile & Run
pyTest:
	@ $(PY3) $(test)/$(trun).py

	
# Clean up
clean:
	del *.exe $(out)/*.o *.out
