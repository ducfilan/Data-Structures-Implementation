class TrieNode:
	def __init__(self, val, is_end=False):
		self.value = val
		self.connected_nodes = []
		self.is_end = is_end

	def set_connected_to_node(self, new_node):
		self.connected_nodes.append(new_node)


root = TrieNode('*')

words = [
    "castle", "cost", "cast", "constant", "love", "lost", "last", "less",
    "lotus", "lasting"
]


def build_trie(root, word):
	current_parent_node = root

	for i, c in enumerate(word):
		nodes_dict = {
		    node.value: node
		    for node in current_parent_node.connected_nodes
		}

		if c not in nodes_dict:
			new_node = TrieNode(c, i + 1 == len(word))
			current_parent_node.set_connected_to_node(new_node)
			current_parent_node = new_node
		else:
			if i + 1 == len(word):
				nodes_dict[c].is_end = True

			current_parent_node = nodes_dict[c]


for word in words:
	build_trie(root, word)


def find_words_start_with(prefix):
	words = []

	def dfs(node, word=''):
		if not word:
			word = prefix[:-1]

		word += node.value

		children = node.connected_nodes

		if node.is_end:
			words.append(word)

		if not children:
			word = ''
		else:
			for child in children:
				dfs(child, word)

	start_node = root

	for c in prefix:
		start_node = next(
		    filter(lambda node: node.value == c, start_node.connected_nodes),
		    None)

	dfs(start_node)

	return words


for word in find_words_start_with('c'):
	print(word)
