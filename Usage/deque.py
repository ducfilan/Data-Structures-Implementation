import unittest
from Implementation.deque import Deque


class MyTestCase(unittest.TestCase):
    def test_something(self):
        d = Deque()
        self.assertEqual(d.is_empty(), True)
        d.add_front('hello')
        d.add_rear('world')
        self.assertEqual(d.size(), 2)
        self.assertEqual(d.remove_front(), 'hello')
        d.add_front(1)
        self.assertEqual(d.remove_front(), 1)
        d.add_rear(2)
        self.assertEqual(d.remove_rear(), 2)
        self.assertEqual(d.size(), 1)


if __name__ == '__main__':
    unittest.main()
