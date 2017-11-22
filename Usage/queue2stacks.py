import unittest
from Implementation.queue2stacks import Queue2Stacks


class MyTestCase(unittest.TestCase):
    def test_something(self):
        q2t = Queue2Stacks()
        q2t.enqueue(1)
        q2t.enqueue(2)
        q2t.enqueue(3)
        self.assertEqual(q2t.size(), 3)
        self.assertEqual(q2t.dequeue(), 1)
        self.assertEqual(q2t.size(), 2)


if __name__ == '__main__':
    unittest.main()
