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
    Prints out the entire tree
    This prints out the tree IN ORDER - Iterative approach
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

    

if __name__ == "__main__":
    node1 = Node(5)
    node2 = Node(4)
    node3 = Node(6)
    node4 = Node(8)
    tree = BST(node1)
    print(tree.insert(node2))
    print(tree.insert(node3))
    print(tree.print_root())
    print(tree.in_order_traversal(tree.root))