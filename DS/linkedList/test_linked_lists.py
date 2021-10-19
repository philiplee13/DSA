import linked_lists
from linkedList import LinkedList, Node

"""
Creating Nodes for Singly linked list for testing
"""
# first_node = Node(1)
# second_node = Node(2)
# third_node = Node(3)
# fourth_node = Node(4)
# fifth_node = Node(5)
# insert_node = Node(6)
# seventh_node = Node(7)
# eighth_node = Node(8)
# ninth_node = Node(9)

"""
Testing for Linked List Question 2.1
"""
def test_remove_duplicates1():
    print("Testing for 1 -> 2 -> 3 -> 1 -> 4, should return True")
    ll = LinkedList()
    ll.push_front(Node(1))
    ll.push_front(Node(2))
    ll.push_front(Node(3))
    ll.push_front(Node(1))
    ll.push_front(Node(4))
    print(ll)
    assert linked_lists.remove_duplicates(ll) == True

