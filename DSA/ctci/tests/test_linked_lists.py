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

"""
3. Delete Middle Node
"""

def test_delete_middle_node():
    lst = sllist(["a","b","c","d","e","f"])
    expected_result = sllist(["a","b","c","e","f"])
    assert linked_lists.delete_middle_node(lst) == expected_result

def test_delete_middle_node_second():
    lst = sllist([1,2,5,3,2,4,1,2])
    expected_result = sllist([1,2,5,3,4,1,2])
    assert linked_lists.delete_middle_node(lst) == expected_result

"""
4. Partition Linked List
"""

def test_partition_linked_list():
    lst = sllist([3,5,8,5,10,2,1])
    expected_result = sllist([3,2,1,5,5,8,10])
    assert linked_lists.partition_linked_list(lst, 5) == expected_result

def test_partition_linked_list_second():
    lst = sllist([9,4,1,7,2,10,12,3])
    expected_result = sllist([4,1,2,3,9,7,10,12])
    assert linked_lists.partition_linked_list(lst, 5) == expected_result