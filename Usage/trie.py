import unittest
from Implementation.Trie import TrieNode, Trie


class MyTestCase(unittest.TestCase):
    def test_something(self):
        trie = Trie(TrieNode('*'))

        dictionary = [
            "castle", "cost", "cast", "constant", "lover", "lotus smile",
            "love", "lost", "last", "less", "lotus", "lasting"
        ]
        trie.build(dictionary)

        self.assertEqual(
            trie.find_words_start_with('lo'),
            ['love', 'lover', 'lotus', 'lotus smile', 'lost'])
        self.assertEqual(
            trie.find_words_start_with('c'),
            ['cast', 'castle', 'cost', 'constant'])
        self.assertEqual(trie.find_words_start_with('cs'), [])


if __name__ == '__main__':
    unittest.main()
