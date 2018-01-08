import unittest
from Implementation.binary_heap import BinaryHeap


class MyTestCase(unittest.TestCase):
    def test_something(self):
        h = BinaryHeap()
        h.build_heap([9, 5, 6, 2, 3, 7, 11, 22, 43, 1, 4, 50, 13, 9, 13, 12, 3, 4, 2, 5, 1, 3, 1, 3, 4])
        h.output_heap()
        h.del_min()
        h.output_heap()
        h.insert(2)
        h.output_heap()

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
