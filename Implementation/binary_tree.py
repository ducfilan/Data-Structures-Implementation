class BinaryTree(object):
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        t = BinaryTree(new_node)

        if self.left_child:
            t.left_child = self.left_child
            self.left_child = t
        else:
            self.left_child = t

    def insert_right(self, new_node):
        t = BinaryTree(new_node)

        if self.right_child:
            t.right_child = self.right_child
            self.right_child = t
        else:
            self.right_child = t

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_root_value(self):
        return self.key

    def set_root_value(self, new_value):
        self.key = new_value

    def pre_order_traverse(self, tree):
        if tree:
            print(tree.get_root_value())
            self.in_order_traverse(tree.get_left_child())
            self.in_order_traverse(tree.get_right_child())

    def in_order_traverse(self, tree):
        if tree:
            self.in_order_traverse(tree.get_left_child())
            print(tree.get_root_value())
            self.in_order_traverse(tree.get_right_child())

    def post_order_traverse(self, tree):
        if tree:
            self.in_order_traverse(tree.get_left_child())
            self.in_order_traverse(tree.get_right_child())
            print(tree.get_root_value())
