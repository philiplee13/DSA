"""
BST Implementation
"""

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
    ITERATIVE METHODS
    """
    
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
    Iterative Approach

    Check if a given node is in the tree
    Return True if it exists
    Return False if it doesn't
    """
    def is_in_tree(self, node: Node):
        if not isinstance(node, Node):
            raise TypeError
        curr = self.root
        while curr is not None:
            if curr.data == node.data:
                return True
            if curr.data > node.data:
                curr = curr.left
            else:
                curr = curr.right
        return False

    """
    Get the height of a tree
        We need to find the max height between the left and right subtrees
        We need to get both the left and right here because they might differ

    Once we get both of their heights - we can find the max between the two
    """
    def get_height(self):
        curr = self.root
        left = 0
        right = 0
        while curr is not None:
            left += 1
            curr = curr.left
        curr = self.root
        while curr is not None:
            right += 1
            curr = curr.right
        return max(left, right)


    """
    RECURSIVE METHODS
    """

    """
    Recursive method for in order traversal
        Left - Node - Right
    """
    def in_order_recursive(self, root: Node):
        pass
        
    """
    Recursive Implementation of Inserting a node
    """
    def insert_recursive(self, root: Node, node: Node):
        pass

    """
    Recursive Approach for checking node is in tree
    """
    def is_in_tree(self, node: Node):
        pass
