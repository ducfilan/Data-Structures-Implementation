import unittest
from Implementation.binary_tree import BinaryTree


class MyTestCase(unittest.TestCase):
    def test_something(self):
        r = BinaryTree('a')
        self.assertEqual(r.get_root_value(), 'a')
        self.assertEqual(r.get_left_child(), None)
        self.assertEqual(r.get_right_child(), None)

        r.insert_left('b')
        self.assertEqual(r.get_left_child().get_root_value(), 'b')

        r.insert_right('c')
        self.assertEqual(r.get_right_child().get_root_value(), 'c')

        r.in_order_traverse(r)
        r.pre_order_traverse(r)
        r.post_order_traverse(r)

        r.get_right_child().set_root_value('hello')
        self.assertEqual(r.get_right_child().get_root_value(), 'hello')


if __name__ == '__main__':
    unittest.main()
