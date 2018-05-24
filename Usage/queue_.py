import unittest
from Implementation.queue_ import Queue


class MyTestCase(unittest.TestCase):
    def test_something(self):
        queue = Queue()
        self.assertEqual(queue.is_empty(), True)
        queue.enqueue(1)
        queue.enqueue("two")
        queue.enqueue(True)
        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.size(), 2)


if __name__ == '__main__':
    unittest.main()
