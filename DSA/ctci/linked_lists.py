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
    while head is not None:
        head = head.next
        trailer = trailer.next
    return trailer.value



"""
3. Delete Middle Node
Implement an algorithm to delete the middle node (ie. any node between the first and last node)
of a singly linked list.

Input - a -> b -> c -> d -> e -> f
Output - a -> b -> d -> e -> f

Let's break this up into two parts
    1. Find a middle node - 
        For this, one way is to traverse the entire linked list and keep count of the length
            Once we hit the end, we traverse the list again until we reach length / 2
        But this is fairly slow - another way to do this is to use two pointers
            One increments by one, and the other increments by two
            By the time our "fast" pointer reaches the end, the "slow" pointer will reach
            the middle of the linked list
        -> A question here is why "two" though? Why not another number?

    2. Once we find the middle node - point the previous node's pointer to the middle node's next
"""
def delete_middle_node(linked_list):
    fast = linked_list.nodeat(0)
    slow = linked_list.nodeat(0)
    prev = None
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        prev = slow
        slow = slow.next
    # delete the middle node - in the llist class "next" is a read only attribute
    # so here we use "remove" instead
    # prev.next = slow.next
    linked_list.remove(slow)
    return linked_list
    
    
"""
4. Partition
Write code to partition a linked list around a value x
All nodes less than x come before all nodes greater than or equal to x
- The partition element can appear anywhere in the "right partition"
It does not need to appear between the left and right partitions

Input - 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1, partition = 5
Output - 3 -> 2 -> 1 -> 5 -> 5 -> 8 -> 10

One way to go about this is to hold 3 different linked list and merge them at the end
    One for the elements less than the partitions
    One for the elements that are equal to the partition (if any)
    One for the elements that are greater than the partition
Then once we finish looping through the original linked list - merge them together
"""
def partition_linked_list(linked_list, partition):
    first = sllist()
    middle = sllist()
    last = sllist()
    result = sllist()
    head = linked_list.nodeat(0)
    # while the head node is not null - iterate through original linked list
    while head is not None:
        # determine if that node should be going in first, middle, or last
        if head.value < partition:
            first.append(head.value)
            head = head.next
        elif head.value > partition:
            last.append(head.value)
            head = head.next
        else:
            middle.append(head.value)
            head = head.next
    # after the loop is done - add all the linked lists together
    result += first
    result += middle
    result += last
    return result