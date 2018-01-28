/**
 * Automated testing of C++ solutions to the Project Euler problems.
 * Using C++ googletest framework.
 *
 * TODO: 
 *   - automatically read the correct answers from an ASCII-file
 *   - automatically read the inputs for Euler problems from ASCII
**/

// Googletest header
#include "gtest/gtest.h"

// Euler templates to test
#include "p001/eu001.hpp"
// #include "p002/eu002.hpp"
// #include "p003/eu003.hpp"



// ------ FIXTURES -------

class Test001 : public testing::Test {
    
    virtual void SetUp() override {
      
        pinp = 1000;
        pans = 233168;
      
    }
    
    public:
   
        int pinp, pans;
   
};
        
        
      
        
        
        
// ------ TESTS -------

// Problem # 001:
TEST_F(Test001, zeroCase) {
  
    ASSERT_EQ(eu001(0), 0);
   
}

TEST_F(Test001, eulerProblemCase) {
  
    ASSERT_EQ(eu001(pinp), pans);
   
}