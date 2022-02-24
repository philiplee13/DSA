"""
BST Implementation
"""

from typing import Type

from numpy import insert


class Node:
    def __init__(self, data: int):
        if not isinstance(data, int):
            raise TypeError
        self.data = data
        self.left = None
        self.right = None

"""
A BST is a tree that is a tree that where the elements have at most two children
    Each element in a BST can only have two children.
    The nodes left child must have a value less than the parent's value
    The nodes right child must have a value greater than the parent's value
            27
           /  \ 
         14    28
        /  \  /  \ 
       10 15  26  30
"""
class BST:

    """
    When we instantiate a tree - it should be created with the root node
    """
    def __init__(self, root: Node):
        if not isinstance(root, Node):
            raise TypeError
        self.root = root

    """
    Prints out the root node
    """
    def print_root(self):
        return f"The root node is {self.root.data}"
    
    """
    Prints out the entire tree
    This prints out the tee IN ORDER - Iterative approach
        In order is Left - Node - Right
    """
    def in_order_traversal(self, root: Node):
        if not isinstance(root, Node):
            raise TypeError
        stack = []
        result = ""
        curr = root
        while curr is not None or len(stack) != 0:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                result += f"{curr.data} "
                curr = curr.right
        return result

    """
    Recursive method for in order traversal
        Left - Node - Right
    """
    def in_order_recursive(self, root: Node):
        if root is None:
            return
        self.in_order_recursive(root.left)
        print(f"{root.data} ")
        self.in_order_recursive(root.right)
        

    """
    Iterative Approach

    Insertion of a node into an already existing tree
    This function will look at the node passed in and determine which side of
        the tree it should be in.
    While the left or right node of the parent is not None
        We need to keep the "parent" node as well for each iteration
            We need this in order to determine where to insert the new node (parent.left or parent.right)
        traverse the tree to find the insertion point
    Once we get to the insertion point - determine if it should be going in the
        left or right subtree
    """
    def insert(self, node: Node):
        if not isinstance(node, Node):
            raise TypeError
        curr = self.root
        parent = None

        if curr is None:
            raise ValueError("Root cannot be None")

        while curr is not None:
            parent = curr
            if node.data < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        if parent.data < node.data:
            parent.right = node
        else:
            parent.left = node
        return f"Inserted the node {node.data}"

    """
    Recursive Implementation of Inserting a node
    """
    def insert_recursive(self, root: Node, node: Node):
        if root is None:
            return node
        if root is not None:
            if node.data < root.data:
                root.left = self.insert_recursive(root.left, node)
            else:
                root.right = self.insert_recursive(root.right, node)
            return root

    

if __name__ == "__main__":
    node1 = Node(5)
    node2 = Node(4)
    node3 = Node(6)
    node4 = Node(8)
    iterative_tree = BST(node1)
    print(iterative_tree.insert(node2))
    print(iterative_tree.insert(node3))
    print(iterative_tree.print_root())
    print(f"Iterative Traversal - {iterative_tree.in_order_traversal(iterative_tree.root)}")
    print("RECURSIVE METHODS")
    recursive_tree = BST(node2)
    recursive_tree.insert_recursive(recursive_tree.root, node4)
    recursive_tree.insert_recursive(recursive_tree.root, node3)
    recursive_tree.in_order_recursive(recursive_tree.root)