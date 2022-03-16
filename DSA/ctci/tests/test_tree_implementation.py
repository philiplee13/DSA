from DSA.ctci import trees_implementation

"""
Iterative Tree Methods
"""

"""
Test add node - in order elements
"""


def test_add_node():
    node1 = trees_implementation.Node(5)
    node2 = trees_implementation.Node(4)
    node3 = trees_implementation.Node(6)
    node4 = trees_implementation.Node(8)
    tree = trees_implementation.BST(node1)
    tree.insert(node2)
    tree.insert(node3)
    tree.insert(node4)
    expected_result = "4 5 6 8 "
    result = tree.in_order_iterative(tree.root)
    assert expected_result == result


"""
Test add node 2 - add in random order elements
"""


def test_add_node2():
    node1 = trees_implementation.Node(5)
    node2 = trees_implementation.Node(4)
    node3 = trees_implementation.Node(6)
    node4 = trees_implementation.Node(8)
    tree = trees_implementation.BST(node1)
    tree.insert(node3)
    tree.insert(node4)
    tree.insert(node2)
    expected_result = "4 5 6 8 "
    result = tree.in_order_iterative(tree.root)
    assert expected_result == result


"""
Test is_in method - this should return true
"""

def test_is_in_tree():
    node1 = trees_implementation.Node(5)
    node2 = trees_implementation.Node(4)
    node3 = trees_implementation.Node(6)
    node4 = trees_implementation.Node(8)
    tree = trees_implementation.BST(node1)
    tree.insert(node3)
    tree.insert(node4)
    tree.insert(node2)
    expected_result = True
    assert expected_result == tree.is_in_tree(node4)


"""
Test is_in method - this should return false
"""

def test_is_in_tree_false():
    node1 = trees_implementation.Node(5)
    node2 = trees_implementation.Node(4)
    node3 = trees_implementation.Node(6)
    node4 = trees_implementation.Node(8)
    node10 = trees_implementation.Node(10)
    tree = trees_implementation.BST(node1)
    tree.insert(node3)
    tree.insert(node4)
    tree.insert(node2)
    expected_result = False
    assert expected_result == tree.is_in_tree(node10)



"""
Test get_height method - this should return 4
"""

def test_get_height():
    node1 = trees_implementation.Node(5)
    node2 = trees_implementation.Node(4)
    node3 = trees_implementation.Node(6)
    node4 = trees_implementation.Node(8)
    node10 = trees_implementation.Node(10)
    tree = trees_implementation.BST(node1)
    tree.insert(node2)
    tree.insert(node3)
    tree.insert(node4)
    tree.insert(node10)
    expected_result = 4
    assert expected_result == tree.get_height(tree.root)


"""
Test get_min method - this should return 4
"""
def test_get_min():
    node1 = trees_implementation.Node(5)
    node2 = trees_implementation.Node(4)
    node3 = trees_implementation.Node(6)
    node4 = trees_implementation.Node(8)
    node10 = trees_implementation.Node(10)
    tree = trees_implementation.BST(node1)
    tree.insert(node2)
    tree.insert(node3)
    tree.insert(node4)
    tree.insert(node10)
    expected_result = 4
    assert expected_result == tree.get_min()

"""
Test get_min method - this should return 2
"""
def test_get_min_second_test():
    node1 = trees_implementation.Node(3)
    node2 = trees_implementation.Node(2)
    node3 = trees_implementation.Node(4)
    node4 = trees_implementation.Node(8)
    node10 = trees_implementation.Node(5)
    tree = trees_implementation.BST(node1)
    tree.insert(node2)
    tree.insert(node3)
    tree.insert(node4)
    tree.insert(node10)
    expected_result = 2
    assert expected_result == tree.get_min()

"""
Test get_max method - this should return 10
"""
def test_get_max():
    node1 = trees_implementation.Node(3)
    node2 = trees_implementation.Node(2)
    node3 = trees_implementation.Node(4)
    node4 = trees_implementation.Node(8)
    node10 = trees_implementation.Node(5)
    tree = trees_implementation.BST(node1)
    tree.insert(node2)
    tree.insert(node3)
    tree.insert(node4)
    tree.insert(node10)
    expected_result = 8
    assert expected_result == tree.get_max()

"""
Test get_max method - this should return 15
"""
def test_get_max_second_test():
    node1 = trees_implementation.Node(3)
    node2 = trees_implementation.Node(2)
    node3 = trees_implementation.Node(4)
    node4 = trees_implementation.Node(8)
    node15 = trees_implementation.Node(15)
    tree = trees_implementation.BST(node1)
    tree.insert(node2)
    tree.insert(node3)
    tree.insert(node4)
    tree.insert(node15)
    expected_result = 15
    assert expected_result == tree.get_max()

"""
Test method for BFS
"""

"""
Before the 1st iteration
    seen = [A]
    q = [A]
    result = ""

1st iteration of the while loop
    seen = [A]
    q = []
    node = A
    result = A
        inside the for loop
        seen = [A, B, C]
        q = [B, C]
2nd iteration of the while loop
    seen = [A, B, C]
    q = [B, C]
    node = B
    result = A B
        inside the for loop
        seen = [A, B, C, D, E]
        q = [C, D, E]
3rd iteration of the while loop
    seen = [A, B, C, D, E]
    q = [D, E]
    node = C
    result = A B C
        inside the for loop
        seen = [A, B, C, D, E, F]
        q = [D, E, F]
... pattern continues for BFS
"""
def test_bfs():
    graph = {
        "A" : ["B","C"],
        "B" : ["D", "E"],
        "C" : ["F"],
        "D" : [],
        "E" : ["F"],
        "F" : []
        }
    expected_result = "A B C D E F "
    result = trees_implementation.bfs(graph, "A")
    assert expected_result == result
