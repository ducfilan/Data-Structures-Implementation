import unittest
from Implementation.stack import Stack


class MyTestCase(unittest.TestCase):
    def test_something(self):
        stack = Stack()
        self.assertEqual(stack.is_empty(), True)
        stack.push(1)
        stack.push("two")
        self.assertEqual(stack.peek(), "two")
        stack.push(True)
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.pop(), True)
        self.assertEqual(stack.size(), 2)


if __name__ == '__main__':
    unittest.main()
