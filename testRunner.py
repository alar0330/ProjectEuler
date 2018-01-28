"""
Automated testing of Python solutions to the Project Euler problems.
Using unittest framework.

TODO: 
    * automatically read the correct answers from an ASCII-file
    * automatically read the inputs for Euler problems from ASCII
"""


import unittest

from p001.eu001 import *
from p002.eu002 import *
from p003.eu003 import *


failed_correct_answer = "WRONG answer to Project Euler Problem"
failed_hint_answer = "WRONG answer to Project Euler Hint"
failed_zero_answer = "WRONG answer to Zero Case"
failed_unity_answer = "WRONG answer to Unity Case"




# ------ FIXTURES -------

class test001(unittest.TestCase):

    # --- Setup
    def setUp(self):
        self.pinp = 1000
        self.pans = 233168
        
    def tearDown(self):
        pass
        
    # --- Tests
    def test_correctAnswer(self):
        self.assertEqual(eu001(self.pinp), self.pans, failed_correct_answer)
        
    def test_zeroCase(self):
        self.assertEqual(eu001(0), 0, failed_zero_answer)
        
        
class test002(unittest.TestCase):

    # --- Setup
    def setUp(self):
        self.pinp = 4*1000*1000
        self.pans = 4613732
        
    def tearDown(self):
        pass
        
    # --- Tests
    def test_correctAnswer(self):
        self.assertEqual(eu002(self.pinp), self.pans, failed_correct_answer)
        
    def test_zeroCase(self):
        self.assertEqual(eu002(0), 0, failed_zero_answer)
        
    def test_correctAnswer_alt(self):
        self.assertEqual(eu002_alt(self.pinp), self.pans, failed_correct_answer)
        
    def test_zeroCase_alt(self):
        self.assertEqual(eu002_alt(0), 0, failed_zero_answer)

        
class test003(unittest.TestCase):

    # --- Setup
    def setUp(self):
        self.pinp = 600851475143
        self.pans = 6857
        
        self.hinp = 13195
        self.hans = 29
        
    def tearDown(self):
        pass
        
    # --- Tests
    def test_correctAnswer(self):
        self.assertEqual(eu003(self.pinp), self.pans, failed_correct_answer)
        
    def test_simpleCase(self):
        self.assertEqual(eu003(self.hinp), self.hans, failed_hint_answer)
        
    def test_selfPrime(self):
        self.assertEqual(eu003(997), 997, "WRONG answer to Self-Prime case")
        
    def test_zeroCase(self):
        self.assertEqual(eu003(0), 0, failed_zero_answer)
        
    def test_zeroCase(self):
        self.assertEqual(eu003(1), 1, failed_unity_answer)
        
    def test_inp100_chk5(self):
        self.assertEqual(eu003(100), 5, "WRONG answer to Input-is-100 case")
        
        
        
        
# ------ RUNNER -------

if __name__ == '__main__':
    unittest.main(verbosity=2)