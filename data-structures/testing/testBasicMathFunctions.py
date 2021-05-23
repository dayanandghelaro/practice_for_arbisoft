import unittest
from basicMathFunctions.basicMathFunctions import *

class TestBasicMathFunctions(unittest.TestCase):
    def test_addition(self):
        self.assertAlmostEqual(addition(2,4), 6)
        self.assertAlmostEqual(addition(-2,-24), -26)
        self.assertAlmostEqual(addition(0,4), 4)
        self.assertAlmostEqual(addition(2.5,4.5), 7.0)
        self.assertAlmostEqual(addition(-2.7,4.8), 2.1)

    
    def test_subtraction(self):
        self.assertAlmostEqual(subtraction(2,4), -2)
        self.assertAlmostEqual(subtraction(-2,-24), 22)
        self.assertAlmostEqual(subtraction(0,4), -4)
        self.assertAlmostEqual(subtraction(2.5,4.5), -2.0)
        self.assertAlmostEqual(subtraction(-2.7,4.8), -7.5)


    def test_multiplication(self):
        self.assertAlmostEqual(multiplication(2,4), 8)
        self.assertAlmostEqual(multiplication(-2,-24), 48)
        self.assertAlmostEqual(multiplication(0,4), 0)
        self.assertAlmostEqual(multiplication(2.5,4.5), 11.25)
        self.assertAlmostEqual(multiplication(-2.7,4.8), -12.96)


    def test_division(self):
        self.assertAlmostEqual(division(2,4), 0.5)
        self.assertAlmostEqual(round(division(-2,-24), 4), 0.0833)
        self.assertAlmostEqual(division(0,4), 0)
        self.assertAlmostEqual(round(division(2.5,4.5), 4), 0.5556)
        self.assertAlmostEqual(round(division(-2.7,4.8), 4), -0.5625)


    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, division, 2,0)
        self.assertRaises(ZeroDivisionError, division, -321,0)

    def test_inputs(self):
        self.assertRaises(TypeError, addition, [], [])
        self.assertRaises(TypeError, addition, 2, [])
        self.assertRaises(TypeError, addition, [], 4)
        self.assertRaises(TypeError, addition, "d", [])
        self.assertRaises(TypeError, addition, 4, "4")
        self.assertRaises(TypeError, addition, True, 2)        
        self.assertRaises(TypeError, subtraction, [], [])
        self.assertRaises(TypeError, subtraction, 2, [])
        self.assertRaises(TypeError, subtraction, [], 4)
        self.assertRaises(TypeError, subtraction, "d", [])
        self.assertRaises(TypeError, subtraction, 4, "4")
        self.assertRaises(TypeError, subtraction, True, 2)
        self.assertRaises(TypeError, multiplication, [], [])
        self.assertRaises(TypeError, multiplication, 2, [])
        self.assertRaises(TypeError, multiplication, [], 4)
        self.assertRaises(TypeError, multiplication, "d", [])
        self.assertRaises(TypeError, multiplication, 4, "4")
        self.assertRaises(TypeError, multiplication, True, 2)
        self.assertRaises(TypeError, division, [], [])
        self.assertRaises(TypeError, division, 2, [])
        self.assertRaises(TypeError, division, [], 4)
        self.assertRaises(TypeError, division, "d", [])
        self.assertRaises(TypeError, division, 4, "4")
        self.assertRaises(TypeError, division, True, 2)
        
        

    

