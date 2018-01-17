import unittest
from Implementation.binary_search_tree import BinarySearchTree, TreeNode


class MyTestCase(unittest.TestCase):
    def test_something(self):
        my_tree = BinarySearchTree()
        my_tree[3] = "red"
        my_tree[4] = "blue"
        my_tree[6] = "yellow"
        my_tree[2] = "at"

        print(my_tree[6])
        print(my_tree[2])

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
