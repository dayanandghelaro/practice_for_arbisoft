from stack import Stack, ValidationError
import unittest


class TestStack(unittest.TestCase):
    def test_stack_initialization(self):
        self.assertRaises(TypeError, Stack, [])
        self.assertRaises(TypeError, Stack, "12")
        self.assertRaises(TypeError, Stack, True)
        self.assertRaises(ValueError, Stack, -1)
        self.assertRaises(ValueError, Stack, 0)

    def test_push_validation(self):
        stack = Stack(1)
        stack.push(12)
        self.assertRaises(TypeError, stack.push, "str")
        self.assertRaises(ValidationError, stack.push, 3)

    def test_stack_empty(self):
        stack = Stack(10)
        self.assertAlmostEqual(stack.isEmpty(), True)
        stack = Stack(1)
        self.assertAlmostEqual(stack.isEmpty(), True)
        stack = Stack(100)
        self.assertAlmostEqual(stack.isEmpty(), True)

    def test_stack_not_empty(self):
        stack = Stack(10)
        stack.push(12)
        self.assertAlmostEqual(stack.isEmpty(), False)
        stack = Stack(1)
        stack.push(12)
        self.assertAlmostEqual(stack.isEmpty(), False)
        stack = Stack(120)
        stack.push(12)
        self.assertAlmostEqual(stack.isEmpty(), False)
        
    def test_stack_full(self):
        stack = Stack(1)
        stack.push(12)
        self.assertAlmostEqual(stack.isFull(), True)
        stack = Stack(10)
        for i in range(10):
            stack.push(i)
        self.assertAlmostEqual(stack.isFull(), True)

    def test_peek(self):
        stack = Stack(12)
        self.assertRaises(ValidationError, stack.peek)
        stack.push(13)
        self.assertAlmostEqual(stack.peek(), 13)
        stack.push(44)
        self.assertAlmostEqual(stack.peek(), 44)
        

    def test_pop(self):
        stack = Stack(2)
        self.assertAlmostEqual(stack.isEmpty(), True)
        self.assertAlmostEqual(stack.isFull(), False)
        self.assertRaises(ValidationError, stack.pop)
        stack.push(13)
        self.assertAlmostEqual(stack.isEmpty(), False)
        stack.push(33)
        self.assertAlmostEqual(stack.isFull(), True)
        self.assertAlmostEqual(stack.peek(), 33)
        self.assertAlmostEqual(stack.pop(), 33)
        self.assertAlmostEqual(stack.peek(), 13)
        self.assertAlmostEqual(stack.pop(), 13)
        self.assertRaises(ValidationError, stack.peek)
        self.assertRaises(ValidationError, stack.pop)
        self.assertAlmostEqual(stack.isEmpty(), True)
        self.assertAlmostEqual(stack.isFull(), False)

    def test_datatype(self):
        stack = Stack(2,str)
        self.assertRaises(TypeError, stack.push, 12)
        self.assertRaises(TypeError, stack.push, True)
        self.assertRaises(TypeError, stack.push, [])
        self.assertRaises(TypeError, stack.push, {})
        stack.push("Pakistan")
        self.assertAlmostEqual(stack.peek(), "Pakistan")
        


