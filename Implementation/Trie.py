class TrieNode:
    def __init__(self, val):
        self.value = val
        self.is_end = False
        self.connected_nodes = []
        
    def set_connected_to_node(self, new_node):
        self.connected_nodes.append(new_node)

    def get_connected_nodes(self):
        return self.connected_nodes

    def get_value(self):
        return self.value

root = TrieNode('*')

words = ["cost", "cast", "constant", "love", "lost", "last"]

def build_trie(root, word):
    current_parrent_node = root
    nodes_dict = { node.get_value(): node for node in current_parrent_node.get_connected_nodes() }
    
    for c in word:
        if c not in nodes_dict:
            new_node = TrieNode(c)
            current_parrent_node.set_connected_to_node(TrieNode(c))
            current_parrent_node = new_node
        else:
            current_parrent_node = nodes_dict[c]

for word in words:
    build_trie(root, word)

for x in root.get_connected_nodes():
    print(x.get_value())
    for y in x.get_connected_nodes():
        print(y.get_value())
		