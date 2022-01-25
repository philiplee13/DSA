"""
All questions here will use the sllist class from llist
llist documentation - https://ajakubek.github.io/python-llist/index.html#llist.sllist
"""
from llist import sllist

"""
1. Remove Dups
Write code to remove duplicates from an unsorted linked list
Input : 3 -> 2 -> 2 -> 1 -> 1
Output : 3 -> 2 -> 1

With a singly linked list - we need to traverse the elements one by one
One option is just to iterate through the linked list - checking if we've already added
that specific element to our linked list that we want to return
    The run time for this is O(n) -> where "n" is the size of the linked list

Because we want to return a linked list - we cannot use a set here - it won't perserve the order
"""

def remove_dups(linked_list):
    result = sllist()
    for i in range(len(linked_list)):
        if linked_list[i] not in result:
            result.append(linked_list[i])
    return result


"""
2. 
"""