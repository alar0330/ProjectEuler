"""
Automated testing of Python solutions to the Project Euler problems.
Using unittest framework.
"""

# import unittest
import unittest


# add parent dir to the search path
import os
import sys
#
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# parse the XML with in-/out-data
import xml.etree.ElementTree as ET
#
root = ET.parse('ans/ProjectEuler.xml').getroot()


# import Project Euler modules
from problems.p001.eu001 import *
from problems.p002.eu002 import *
from problems.p003.eu003 import *
from problems.p004.eu004 import *
from problems.p005.eu005 import *
from problems.p006.eu006 import *
from problems.p007.eu007 import *




# ------- COMMON ERROR MSGS -------

failed_correct_answer = "WRONG answer to Project Euler Problem"
failed_hint_answer = "WRONG answer to Project Euler Hint"
failed_zero_answer = "WRONG answer to Zero Case"
failed_unity_answer = "WRONG answer to Unity Case"




# ------ FIXTURES -------

class test001(unittest.TestCase):

    # --- Setup
    def setUp(self):
        pnum = 1
        pstr = "p{:03d}".format(pnum)
        #    
        self.qinp = int(root.find(pstr).find('question').find('input').text)
        self.qans = int(root.find(pstr).find('question').find('answer').text)
        #
        self.hinp = int(root.find(pstr).find('hint').find('input').text)
        self.hans = int(root.find(pstr).find('hint').find('answer').text)

    def tearDown(self):
        pass
        
    # --- Tests
    def test_correctAnswer(self):
        self.assertEqual(eu001(self.qinp), self.qans, failed_correct_answer)
        
    def test_hintCase(self):
        self.assertEqual(eu001(self.hinp), self.hans, failed_hint_answer)
        
    def test_zeroCase(self):
        self.assertEqual(eu001(0), 0, failed_zero_answer)
        
        
class test002(unittest.TestCase):

    # --- Setup
    def setUp(self):
        pnum = 2
        pstr = "p{:03d}".format(pnum)
        #    
        self.qinp = int(root.find(pstr).find('question').find('input').text)
        self.qans = int(root.find(pstr).find('question').find('answer').text)
        #
        self.hinp = int(root.find(pstr).find('hint').find('input').text)
        self.hans = int(root.find(pstr).find('hint').find('answer').text)
        
    def tearDown(self):
        pass
        
    # --- Tests
    def test_correctAnswer(self):
        self.assertEqual(eu002(self.qinp), self.qans, failed_correct_answer)
        
    def test_hintCase(self):
        self.assertEqual(eu002(self.hinp), self.hans, failed_hint_answer)
        
    def test_zeroCase(self):
        self.assertEqual(eu002(0), 0, failed_zero_answer)
        
    def test_correctAnswer_alt(self):
        self.assertEqual(eu002_alt(self.qinp), self.qans, failed_correct_answer)
        
    def test_hintCase_alt(self):
        self.assertEqual(eu002_alt(self.hinp), self.hans, failed_hint_answer)
        
    def test_zeroCase_alt(self):
        self.assertEqual(eu002_alt(0), 0, failed_zero_answer)

        
class test003(unittest.TestCase):

    # --- Setup
    def setUp(self):
        pnum = 3
        pstr = "p{:03d}".format(pnum)
        #    
        self.qinp = int(root.find(pstr).find('question').find('input').text)
        self.qans = int(root.find(pstr).find('question').find('answer').text)
        #
        self.hinp = int(root.find(pstr).find('hint').find('input').text)
        self.hans = int(root.find(pstr).find('hint').find('answer').text)
        
    def tearDown(self):
        pass
        
    # --- Tests
    def test_correctAnswer(self):
        self.assertEqual(eu003(self.qinp), self.qans, failed_correct_answer)
        
    def test_hintCase(self):
        self.assertEqual(eu003(self.hinp), self.hans, failed_hint_answer)
        
    def test_selfPrime(self):
        self.assertEqual(eu003(997), 997, "WRONG answer to Self-Prime case")
        
    def test_zeroCase(self):
        self.assertEqual(eu003(0), 0, failed_zero_answer)
        
    def test_unityCase(self):
        self.assertEqual(eu003(1), 1, failed_unity_answer)
        
    def test_inp100_chk5(self):
        self.assertEqual(eu003(100), 5, "WRONG answer to Input-is-100 case")
 
 
class test004(unittest.TestCase):

    # --- Setup
    def setUp(self):
        pnum = 4
        pstr = "p{:03d}".format(pnum)
        #    
        self.qinp = int(root.find(pstr).find('question').find('input').text)
        self.qans = int(root.find(pstr).find('question').find('answer').text)
        #
        self.hinp = int(root.find(pstr).find('hint').find('input').text)
        self.hans = int(root.find(pstr).find('hint').find('answer').text)
        
    def tearDown(self):
        pass
        
    # --- Tests
    def test_correctAnswer(self):
        self.assertEqual(eu004(self.qinp), self.qans, failed_correct_answer)
        
    def test_hintCase(self):
        self.assertEqual(eu004(self.hinp), self.hans, failed_hint_answer)
        
    def test_unityCase(self):
        self.assertEqual(eu004(1), 9, failed_unity_answer)
        
        
class test005(unittest.TestCase):

    # --- Setup
    def setUp(self):
        pnum = 5
        pstr = "p{:03d}".format(pnum)
        #    
        self.qinp = int(root.find(pstr).find('question').find('input').text)
        self.qans = int(root.find(pstr).find('question').find('answer').text)
        #
        self.hinp = int(root.find(pstr).find('hint').find('input').text)
        self.hans = int(root.find(pstr).find('hint').find('answer').text)
        
    def tearDown(self):
        pass
        
    # --- Tests
    def test_correctAnswer(self):
        self.assertEqual(eu005(self.qinp), self.qans, failed_correct_answer)
        
    def test_hintCase(self):
        self.assertEqual(eu005(self.hinp), self.hans, failed_hint_answer)
        
    def test_unityCase(self):
        self.assertEqual(eu005(1), 1, failed_unity_answer)
        
        
class test006(unittest.TestCase):

    # --- Setup
    def setUp(self):
        pnum = 6
        pstr = "p{:03d}".format(pnum)
        #    
        self.qinp = int(root.find(pstr).find('question').find('input').text)
        self.qans = int(root.find(pstr).find('question').find('answer').text)
        #
        self.hinp = int(root.find(pstr).find('hint').find('input').text)
        self.hans = int(root.find(pstr).find('hint').find('answer').text)
        
    def tearDown(self):
        pass
        
    # --- Tests
    def test_correctAnswer(self):
        self.assertEqual(eu006(self.qinp), self.qans, failed_correct_answer)
        
    def test_hintCase(self):
        self.assertEqual(eu006(self.hinp), self.hans, failed_hint_answer)
        
    def test_unityCase(self):
        self.assertEqual(eu006(1), 0, failed_unity_answer)
        
    def test_correctAnswer_alt(self):
        self.assertEqual(eu006_alt(self.qinp), self.qans, failed_correct_answer)
        
    def test_hintCase_alt(self):
        self.assertEqual(eu006_alt(self.hinp), self.hans, failed_hint_answer)
        
        
class test007(unittest.TestCase):

    # --- Setup
    def setUp(self):
        pnum = 7
        pstr = "p{:03d}".format(pnum)
        #    
        self.qinp = int(root.find(pstr).find('question').find('input').text)
        self.qans = int(root.find(pstr).find('question').find('answer').text)
        #
        self.hinp = int(root.find(pstr).find('hint').find('input').text)
        self.hans = int(root.find(pstr).find('hint').find('answer').text)
        
    def tearDown(self):
        pass
        
    # --- Tests
    def test_correctAnswer(self):
        self.assertEqual(eu007(self.qinp), self.qans, failed_correct_answer)
        
    def test_hintCase(self):
        self.assertEqual(eu007(self.hinp), self.hans, failed_hint_answer)
        
        
# ------ RUNNER -------

if __name__ == '__main__':
    unittest.main(verbosity=2)
