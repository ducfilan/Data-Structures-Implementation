class TrieNode:
    def __init__(self, val, is_end=False):
        self.value = val
        self.is_end = is_end
        self.connected_nodes = []

    def set_connected_to_node(self, new_node):
        self.connected_nodes.append(new_node)

    def get_connected_nodes(self):
        return self.connected_nodes

    def get_value(self):
        return self.value

    def set_is_end(self, is_end):
        self.is_end = is_end


root = TrieNode('*')

words = ["cost", "cast", "constant", "love", "lost", "last"]


def build_trie(root, word):
    current_parent_node = root
    nodes_dict = {node.get_value(): node for node in current_parent_node.get_connected_nodes()}

    for i, c in enumerate(word):
        if c not in nodes_dict:
            new_node = TrieNode(c, i + 1 == len(word))
            current_parent_node.set_connected_to_node(new_node)
            current_parent_node = new_node
        else:
            if i + 1 == len(word):
                nodes_dict[c].set_is_end(True)

            current_parent_node = nodes_dict[c]


for word in words:
    build_trie(root, word)


def find_words_start_with(prefix):
    words = []

    current_parent_node = root
    nodes_dict = {node.get_value(): node for node in current_parent_node.get_connected_nodes()}

    for i, c in enumerate(prefix):
        if c in nodes_dict:
            current_parent_node = nodes_dict[c]

    for node in current_parent_node.get_connected_nodes():
        words.append(prefix + node.get_value())

    return words
