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
2. Return kth to last
Implement an algorithm to find the Kth to the last element of a singly linked list

We're assuming that we're going to recieve a parameter that is not bigger than the
singly linked list. We also assume that we don't know the length of the linked list

Input - 3 -> 2 -> 2 -> 1 -> 4 -> 5, find the "5th" to the last element of the linked list
Output - 2

If we were told to find the "2nd" to the last element - the output here would be 4

For this solution - we'll use two pointers here.
    One pointer will start off being "k" nodes ahead of the second pointer
    The second pointer will start at the head node
    We will iterate until our first pointer (the one that starts at k) reaches the end
    At that point - we return our second pointer - which will be "k" nodes from the end
"""

def return_kth_node(linked_list, kth_node):
    first = kth_node
    head = linked_list.nodeat(first)
    trailer = linked_list.nodeat(0)
    while head != None:
        head = head.next
        trailer = trailer.next
    return trailer.value

