from DSA.ctci import trees

"""
Iterative Tree Methods
"""

"""
Test add node - in order elements
"""


def test_add_node():
    node1 = trees.Node(5)
    node2 = trees.Node(4)
    node3 = trees.Node(6)
    node4 = trees.Node(8)
    tree = trees.BST(node1)
    tree.insert(node2)
    tree.insert(node3)
    tree.insert(node4)
    expected_result = "4 5 6 8 "
    result = tree.in_order_traversal(tree.root)
    assert expected_result == result


"""
Test add node 2 - add in random order elements
"""


def test_add_node2():
    node1 = trees.Node(5)
    node2 = trees.Node(4)
    node3 = trees.Node(6)
    node4 = trees.Node(8)
    tree = trees.BST(node1)
    tree.insert(node3)
    tree.insert(node4)
    tree.insert(node2)
    expected_result = "4 5 6 8 "
    result = tree.in_order_traversal(tree.root)
    assert expected_result == result


"""
Test is_in method - this should return true
"""

def test_is_in_tree():
    node1 = trees.Node(5)
    node2 = trees.Node(4)
    node3 = trees.Node(6)
    node4 = trees.Node(8)
    tree = trees.BST(node1)
    tree.insert(node3)
    tree.insert(node4)
    tree.insert(node2)
    expected_result = True
    assert expected_result == tree.is_in_tree(node4)


"""
Test is_in method - this should return false
"""

def test_is_in_tree_false():
    node1 = trees.Node(5)
    node2 = trees.Node(4)
    node3 = trees.Node(6)
    node4 = trees.Node(8)
    node10 = trees.Node(10)
    tree = trees.BST(node1)
    tree.insert(node3)
    tree.insert(node4)
    tree.insert(node2)
    expected_result = False
    assert expected_result == tree.is_in_tree(node10)



"""
Test get_height method - this should return 4
"""

def test_get_height():
    node1 = trees.Node(5)
    node2 = trees.Node(4)
    node3 = trees.Node(6)
    node4 = trees.Node(8)
    node10 = trees.Node(10)
    tree = trees.BST(node1)
    tree.insert(node2)
    tree.insert(node3)
    tree.insert(node4)
    tree.insert(node10)
    expected_result = 4
    assert expected_result == tree.get_height()

