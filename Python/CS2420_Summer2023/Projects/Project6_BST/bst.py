class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    """
    BST class must be generic is the sense that it can store and operate on any kind of data items
    that are comparable. For instance, it should be possible to store a set of integers in one instance
    of your BST class, and a set of strings in another (without modification).
    """
    def __init__(self):
        self.root = None

    def print_tree(self, order="inorder"):
        """
        Return printable string representation of tree data.
        """
        def print_inorder(node):
            if node is not None:
                print_inorder(node.left)
                print(node.data, end=" ")
                print_inorder(node.right)

        def print_preorder(node):
            if node is not None:
                print(node.data, end=" ")
                print_preorder(node.left)
                print_preorder(node.right)

        def print_postorder(node):
            if node is not None:
                print_postorder(node.left)
                print_postorder(node.right)
                print(node.data, end=" ")

        print_function = {"inorder": print_inorder,
                          "preorder": print_preorder,
                          "postorder": print_postorder}.get(order, print_inorder)

        print(f"{order}".capitalize())
        print_function(self.root)
        print("\n")

    def size(self):
        """
        Return the number of nodes in the tree.
        """
        def internal_recursion(node):
            if node is None:
                return 0
            else:
                return internal_recursion(node.left) + internal_recursion(node.right) + 1

        return internal_recursion(self.root)

    def is_empty(self):
        """
        Return True if there aren’t any nodes in the tree, False otherwise.
        """
        return self.root is None

    def height(self):
        """
        Return the height of the tree,
        defined as the length of the path from the root to its deepest leaf.
        A tree with zero nodes has a height of -1.
        """
        def internal_recursion(node):
            if node is None:
                return -1
            else:
                left_height = internal_recursion(node.left)
                right_height = internal_recursion(node.right)
                return max(left_height, right_height) + 1

        return internal_recursion(self.root)

    def add(self, item):
        """
        Add item to the tree.
        Return the modified tree.
        """
        def internal_recursion(node):
            if node is None:
                return Node(item)
            if item < node.data:
                node.left = internal_recursion(node.left)
            else:
                node.right = internal_recursion(node.right)
            return node

        self.root = internal_recursion(self.root)
        return self.root

    def remove(self, item):
        """
        Remove item from the tree if it exists,
        if not – do nothing.
        Return the resulting tree.
        """
        def find_min(node):
            return find_min(node.left) if node.left else node

        def internal_recursion(node):
            if node is None:
                return None
            if item < node.data:
                node.left = internal_recursion(node.left)
            elif item > node.data:
                node.right = internal_recursion(node.right)
            else:
                if node.left and node.right:
                    temp = find_min(node.right)
                    node.data = temp.data
                    node.right = internal_recursion(node.right)
                elif node.left:
                    node = node.left
                elif node.right:
                    node = node.right
                else:
                    node = None
            return node

        self.root = internal_recursion(self.root)
        return self.root

    def find(self, item):
        """
        Return the matched item.
        If item is not in the tree, raise a ValueError.
        """
        def internal_recursion(node):
            if node is None:
                raise ValueError(f"Item not found: {item}")
            if item < node.data:
                return internal_recursion(node.left)
            elif item > node.data:
                return internal_recursion(node.right)
            else:
                return node.data

        return internal_recursion(self.root)

    def inorder(self):
        """
        Return a list with the data items in order of inorder traversal.
        """
        def internal_recursion(node):
            return internal_recursion(node.left) + [node.data] + internal_recursion(node.right) if node else []

        return internal_recursion(self.root)

    def preorder(self):
        """
        Return a list with the data items in order of preorder traversal.
        """
        def internal_recursion(node):
            return [node.data] + internal_recursion(node.left) + internal_recursion(node.right) if node else []

        return internal_recursion(self.root)

    def postorder(self):
        """
        Return a list with the data items in order of postorder traversal.
        """
        def internal_recursion(node):
            return internal_recursion(node.left) + internal_recursion(node.right) + [node.data] if node else []

        return internal_recursion(self.root)
