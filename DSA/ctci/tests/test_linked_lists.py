from DSA.ctci import linked_lists
from llist import sllist

"""
1. Remove Dups
"""

def test_remove_dups():
    lst = sllist([3,2,2,1,1])
    expected_result = sllist([3,2,1])
    assert linked_lists.remove_dups(lst) == expected_result

def test_remove_dups_second_test():
    lst = sllist([1,2,3,3,2,1])
    expected_result = sllist([1,2,3])
    assert linked_lists.remove_dups(lst) == expected_result

"""
2. Return kth to last element
"""

def test_return_kth_node():
    lst = sllist([3,2,2,1,4,5])
    expected_result = 2
    assert linked_lists.return_kth_node(lst, 5) == expected_result

def test_return_kth_node_second():
    lst = sllist([3,2,2,1,4,5])
    expected_result = 4
    assert linked_lists.return_kth_node(lst,2) == expected_result