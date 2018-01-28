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


wrongEulerAnswer = "Wrong Project Euler answer"
wrongZeroAnswer = "Wrong Zero Case answer"




# ------ FIXTURES -------

class test001(unittest.TestCase):

    # --- Setup
    def setUp(self):
        self.inp = 1000
        self.ans = 233168
        
    def tearDown(self):
        pass
        
    # --- Tests
    def test_correctAnswer(self):
        self.assertEqual(eu001(self.inp), self.ans, wrongEulerAnswer)
        
    def test_zeroCase(self):
        self.assertEqual(eu001(0), 0, wrongZeroAnswer)
        
        
class test002(unittest.TestCase):

    # --- Setup
    def setUp(self):
        self.inp = 4*1000*1000
        self.ans = 4613732
        
    def tearDown(self):
        pass
        
    # --- Tests
    def test_correctAnswer(self):
        self.assertEqual(eu002(self.inp), self.ans, wrongEulerAnswer)
        
    def test_zeroCase(self):
        self.assertEqual(eu002(0), 0, wrongZeroAnswer)
        
    def test_correctAnswer_alt(self):
        self.assertEqual(sum(eu002_alt(self.inp)), self.ans, wrongEulerAnswer)
        
    def test_zeroCase_alt(self):
        self.assertEqual(sum(eu002_alt(0)), 0, wrongZeroAnswer)

        
        
        
# ------ RUNNER -------

if __name__ == '__main__':
    unittest.main(verbosity=2)