from queue import Queue, ValidationError
import unittest

class TestQueue(unittest.TestCase):
    def test_queue_initialization(self):
        self.assertRaises(TypeError, Queue, [])
        self.assertRaises(TypeError, Queue, "str")
        self.assertRaises(TypeError, Queue, True)
        self.assertRaises(TypeError, Queue, {})
        self.assertRaises(ValueError, Queue, -1)
        self.assertRaises(ValueError, Queue, 0)


    def test_empty_queue(self):
        queue = Queue(1)
        self.assertAlmostEqual(queue.isFull(), False)
        self.assertAlmostEqual(queue.isEmpty(), True)
        queue.enqueue(12)
        self.assertAlmostEqual(queue.isFull(), True)
        self.assertAlmostEqual(queue.isEmpty(), False)

    def test_dequeue(self):
        queue = Queue(3)
        queue.enqueue(12)
        queue.enqueue(1)
        self.assertAlmostEqual(queue.dequeue(), 12)
        self.assertAlmostEqual(queue.dequeue(), 1)
        self.assertRaises(ValidationError, queue.dequeue)
        self.assertAlmostEqual(queue.isEmpty(), True)

    def test_datatype(self):
        queue = Queue(3,str)
        self.assertRaises(TypeError, queue.enqueue,12)
        queue.enqueue("Pakistan")
        queue.enqueue("Sindh")
        self.assertAlmostEqual(queue.dequeue(), "Pakistan")

        
