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
#include "../problems/p001/eu001.hpp"
// #include "../problems/p002/eu002.hpp"
// #include "../problems/p003/eu003.hpp"



// ------ FIXTURES -------

class Test001 : public testing::Test {
    
    virtual void SetUp() override {
        
        // Question input / answer
        qinp = 1000;
        qans = 233168;
        
        // Hint input / answer
        hinp = 10;
        hans = 23;
     
    }
    
    public:
   
        int qinp, qans, hinp, hans;
   
};
        
        
      
        
        
        
// ------ TESTS -------

// Problem # 001:
TEST_F(Test001, zeroCase) {
  
    ASSERT_EQ(eu001(0), 0);
   
}

TEST_F(Test001, eulerProblemCase) {
  
    ASSERT_EQ(eu001(qinp), qans);
   
}

TEST_F(Test001, eulerHintCase) {
  
    ASSERT_EQ(eu001(hinp), hans);
   
}