class TreeNode(object):
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left_child or self.right_child)

    def has_any_children(self):
        return self.left_child or self.right_child

    def has_both_children(self):
        return self.left_child and self.right_child

    def replace_node_data(self, key, val, right, left):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)

        self.size += 1

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, self.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, self.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)

    def __setitem__(self, key, value):
        self._put(key, value)

    def get(self, key):
        if self.root:
            node = self._get(key, self.root)
            if node:
                return node.payload
            return None

        return None

    def _get(self, key, current_node):
        if key == current_node.key:
            return current_node

        if key < current_node.key:
            if current_node.has_left_child():
                return self._get(key, current_node.left_child)
        else:
            if current_node.has_right_child():
                return self._get(key, current_node.right_child)

        return None

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return True if self._get(key, self.root) else False

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError('Error! Key is not found in the tree!')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError('Error! Key is not found in the tree!')

    def __del__(self, key):
        self.delete(key)

    def find_min_child(self, current_node):
        while current_node.left_child:
            current_node = current_node.left_child

        return current_node

    def remove(self, node_to_remove):
        if node_to_remove.is_leaf():
            if node_to_remove == node_to_remove.parent.left_child:
                node_to_remove.parent.left_child = None
            else:
                node_to_remove.parent.right_child = None
        elif not node_to_remove.has_both_children():
            if node_to_remove.parent:
                if node_to_remove.is_left_child():
                    if node_to_remove.has_left_child():
                        node_to_remove.parent.left_child = node_to_remove.left_child
                        node_to_remove.left_child.parent = node_to_remove.parent
                    else:
                        node_to_remove.parent.left_child = node_to_remove.right_child
                        node_to_remove.right_child.parent = node_to_remove.parent
                else:
                    if node_to_remove.has_left_child():
                        node_to_remove.parent.right_child = node_to_remove.left_child
                        node_to_remove.left_child.parent = node_to_remove.parent
                    else:
                        node_to_remove.parent.right_child = node_to_remove.right_child
                        node_to_remove.right_child.parent = node_to_remove.parent
            else:
                node_to_remove.replace_node_data(node_to_remove.left_child.key,
                                                 node_to_remove.left_child.payload,
                                                 node_to_remove.right_child,
                                                 node_to_remove.left_child)
        else:
            node_to_replace = self.find_min_child(node_to_remove.right_child)
            if node_to_replace.is_leaf():
                if node_to_replace.is_left_child():
                    node_to_replace.parent.left_child = None
                else:
                    node_to_replace.parent.right_child = None
            else:
                if node_to_replace.has_right_child():
                    node_to_replace.right_child.parent = node_to_replace.parent
                    if node_to_replace.is_left_chid():
                        node_to_replace.parent.left_child = node_to_replace.right_child
                    else:
                        node_to_replace.parent.right_child = node_to_replace.right_child
                else:
                    node_to_replace.left_child.parent = node_to_replace.parent
                    if node_to_replace.is_left_chid():
                        node_to_replace.parent.left_child = node_to_replace.left_child
                    else:
                        node_to_replace.parent.right_child = node_to_replace.left_child

        node_to_remove.key = node_to_replace.key
        node_to_remove.payload = node_to_replace.payload

        self.size -= 1
