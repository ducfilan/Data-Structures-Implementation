import unittest
from Implementation.binary_heap import BinaryHeap


class MyTestCase(unittest.TestCase):
    def test_something(self):
        h = BinaryHeap()
        h.build_heap([9, 5, 6, 2, 3, 7, 11, 22, 43, 1, 4, 50, 13, 9, 13, 12, 3, 4, 2, 5, 1, 3, 1, 3, 4])
        self.assertEqual(' '.join(map(str, h.heap_list)), '0 1 1 3 2 1 4 9 3 2 5 3 6 13 11 13 12 22 4 43 5 9 3 4 50 7')
        h.del_min()
        self.assertEqual(' '.join(map(str, h.heap_list)), '0 1 1 3 2 3 4 9 3 2 5 3 6 13 11 13 12 22 4 43 5 9 7 4 50')
        h.insert(2)
        self.assertEqual(' '.join(map(str, h.heap_list)), '0 1 1 2 2 3 3 9 3 2 5 3 4 13 11 13 12 22 4 43 5 9 7 4 50 6')


if __name__ == '__main__':
    unittest.main()
