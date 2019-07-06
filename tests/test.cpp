/**
 * Automated testing of C++ solutions to the Project Euler problems.
 * Using C++ googletest framework.
 *
 * TODO: 
 *   - automatically read the correct answers from an YAML-file
 *   - automatically read the inputs for Euler problems from YAML
**/

// Googletest header
#include "gtest/gtest.h"


// Euler templates to test
#include "../problems/p001/solution.hpp"
// #include "../problems/p002/solution.hpp"
// #include "../problems/p003/solution.hpp"
#include "../problems/p004/solution.hpp"



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

class Test004 : public testing::Test {
    
    virtual void SetUp() override {
        
        // Question input / answer
        qinp = 3;
        qans = 906609;
        
        // Hint input / answer
        hinp = 2;
        hans = 9009;
     
    }
    
    public:
   
        int qinp, qans;
        int hinp, hans;
   
};
        
        
      
        
        
        
// ------ TESTS -------

// Problem # 001:
TEST_F(Test001, zeroCase) {
  
    ASSERT_EQ(p001(0), 0);
   
}

TEST_F(Test001, eulerQuestionCase) {
  
    ASSERT_EQ(p001(qinp), qans);
   
}

TEST_F(Test001, eulerHintCase) {
  
    ASSERT_EQ(p001(hinp), hans);
   
}

// Problem # 004:
TEST_F(Test004, eulerHintCase) {
  
    ASSERT_EQ(p004(hinp), hans);
   
}

TEST_F(Test004, eulerQuestionCase) {
  
    ASSERT_EQ(p004(qinp), qans);
   
}

TEST_F(Test004, unityCase) {
  
    ASSERT_EQ(p004(1), 9);
   
}