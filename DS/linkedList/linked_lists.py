"""
Working through Chapter 2 of Linked Lists in CTCI
"""

"""
Linked List 2.1 - Remove Dups
Write code to remove duplicates from an unsorted linked list
    Return False if the linked list contains no duplicates
    Return True if we are able to remove duplicates
"""

def remove_duplicates(linkedList):
    node = linkedList.head
    s = set()
    while node != None:
        if node.data not in s:
            s.add(node.data)
            node = node.next
        else:
            return True
    return False


"""
Linked List 2.2
"""