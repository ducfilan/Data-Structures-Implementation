import unittest
from Implementation.deque import Deque


class MyTestCase(unittest.TestCase):
    def test_something(self):
        d = Deque()
        d.add_front('hello')
        d.add_rear('world')
        self.assertEqual(d.size(), 2)
        self.assertEqual(d.remove_front(), 'hello')
        self.assertEqual(d.remove_rear(), 'world')
        self.assertEqual(d.size(), 0)


if __name__ == '__main__':
    unittest.main()
