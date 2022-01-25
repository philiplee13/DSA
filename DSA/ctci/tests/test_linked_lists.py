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