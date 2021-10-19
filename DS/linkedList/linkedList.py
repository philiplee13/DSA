"""
This file will be implementing singly linked lists from scratch
Let's start off by creating a node class
"""

"""
Node Class
Used to create each Node in the linked list
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    """
    Representation of Node Class
    """
    def __repr__(self):
        return f"The current data is {self.data} and the next node is {self.next}"
"""
LinkedList Class
"""
class LinkedList:
    def __init__(self):
        self.head = None

    """
    Representation of LinkedList Class
    """
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(map(str,nodes))
    """
    Function to push elements to the front of the linked list
    The running time of this method is O(1) -> this is because we're just adding a node to the front of the linked list
    """
    def push_front(self,node):
        node.next = self.head
        self.head = node

    """
    Function to return the size of the linked list
    We need to traverse the entire list to return the size.
    The running time of this method is O(n) where "n" is the size of the linked list

    One way to simplify this is to hold the "size" variable within the LinkedList __init__ method itself and increment
    everytime we add a node
    That way we can just return the "size" attribute
    """
    def size(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return f"Size of Linked List is {count}"
    
    """
    Function to return a boolean value if the linked list is empty or not
    For this we just need to check if the head is empty or not
    The running time of this is O(1) -> this is because all we're doing is checking the head of the linked list
    """
    def is_empty(self):
        if self.head is None:
            return True
        return False

    """
    Function to find the element at a given index
    For this we need to traverse the linked list until we reach the specific index
    Once we find the index - return the value at that node
    The running time for this is O(n) -> where "n" is the number of nodes we need to traverse until we find our index
    The worst case here is traversing until the end of the linked list - and we still don't find a match
    """
    def value_at(self, index):
        node = self.head
        count = 0
        while node is not None:
            if count != index:
                count += 1
                node = node.next
            else:
                return f"The index is {count}, the data at this node is {node.data}"

    """
    Function to pop off the front element of the linked list
    We need to pop off our "head" -> and then assign our next element to be our new head
    The running time for this is O(1) -> it's constant because all we're doing is popping off our first node
    """
    def pop_front(self):
        temp = self.head
        self.head = temp.next
        return f"Our old head was {temp.data}, our new head is {self.head.data}"

    """
    Function to push an element to the end of the linked list
    For this we need to traverse the entire linked list - once we reach the end we can append it
    The running time for this is O(n) -> where "n" is the size of the linked list
    """
    def push_back(self,value):
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = value
        return f"Added {value.data} to the end of the linked list"

    """
    Function to pop off the last element of the linked list
    For this we need to traverse the entire linked list again - once we reach the end we can remove the end node
    We also need to keep track of a "prev" node to set that pointer to "None"
    The running time for this is O(n) -> where "n" is the size of the linked list
    """
    def pop_back(self):
        node = self.head
        temp = node
        while node.next is not None:
            prev = node
            node = node.next
        prev.next = None
        return f"Dropped the last node {node.data}"

    """
    Function to return the front of the linked list
    We can just return the self.head here
    This will be constant time because we're accessing the very first element of the linked list
    """
    def front(self):
        return self.head.data

    """
    Function to return the end of the linked list
    We need to traverse the entire linked list - once we reach the end we can return the last node
    This will be O(n) -> where "n" is the size of the linked list
    """
    def back(self):
        node = self.head
        while node.next is not None:
            node = node.next
        return f"The last node of the linked list is {node.data}"

    """
    Function to insert a value at a certain index to a linked list
    We'll need to traverse the linked list until we find our index
    Once we do - we need to set the previous pointer to our new value
    As well as set our new values next to our previous element's "next" value
    This will be O(n) -> where "n" is the number of traversals in order to find our index
    insert(2, 3)
    """
    def insert(self,index,value):
        node = self.head
        curr_index = 0
        while curr_index != index:
            prev = node
            node = node.next
            curr_index += 1
        prev.next = value
        value.next = node

    """
    Function to erase a node at a given index.
    We need to traverse the linked list until we find our index.
    Once we do, we need to set our "previous" element next pointer to our element's "next" node
    This will be O(n) -> where "n" is the time it takes to find our node at a given index
    """
    def erase(self, index):
        node = self.head
        curr_index = 0
        while curr_index != index:
            prev = node
            node = node.next
            curr_index += 1
            temp = node
        prev.next = node.next
        return f"We deleted the node {temp.data}"

    """
    Function that pops off the node with the given value
    We need to traverse the linked list until we find the node with the given value.
    Once we find it, set the value's previous node to point to the value's next node.
    This will be O(n) -> where "n" is the time it takes to find our node with the given value
    """
    def remove_value(self, value):
        node = self.head
        while node.data != value:
            prev = node
            node = node.next
        prev.next = node.next
        return f"We've removed the value {value}"

    """
    Function that reverses the linked list.
    We need to keep track of our previous node, and our current node
    We traverse the linked list - while traversing we take the following steps:
        1. Set a "next" pointer to our current nodes "next"
        2. Set our current.next pointer to our "prev"
        3. Set our current element to our next
    Then after we're done traversing - we set our head to our "prev" element
    What we're essentially doing here is "reversing" the pointers while traversing the list
    This runs in O(n) time -> where "n" is the time that it takes for us to traverse the linked list
    So let's say that we have the following:
    Null -> 1 -> 2 -> 3 -> Null
        In the first iteration we have the following:
            prev = None
            current = 1
                We then go into our loop:
                1st iteration
                    next = 2
                    current.next = None
                    prev = 1
                    current = 2
                The linked list looks like this now:
                Null <- 1 2 -> 3 -> Null
                2nd iteration
                    next = 3
                    current.next = 1
                    prev = 2
                    current = 3
                The linked list looks like this now:
                Null <- 1 <- 2 3 -> Null
                3rd iteration
                    next = Null
                    current.next = 2
                    prev = 3
                    current = Null
                The linked list looks like this now:
                Null <- 1 <- 2 <- 3 -> Null
                4th iteration
                    Doesn't go into loop -> the criteria of current != None is false
                So now we set the head to "prev" -> which was "3"
                Now the Linked list looks like this:
                Null <- 1 <- 2 <- 3
                    3 is our new "head" now
    """
    def reverse(self):
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    """
    Function to find the distance from a given position to the end of the linked list.
    We'll first need to traverse the list until we find the given position
    Then from there keep track of the difference between that position and the end of the linked list.
    This will take O(n) -> we still need to traverse the entire linked list.
    """
    def distance_from_end(self, index):
        node = self.head
        position = 0
        distance = 0
        while node != None:
            if position >= index:
                distance += 1
            node = node.next
            position += 1
        return f"The distance from index {index} to the end of the linked list is {distance}"

def main():
    ll = LinkedList()
    print(ll.is_empty())
    first_node = Node(1)
    second_node = Node(2)
    third_node = Node(3)
    fourth_node = Node(4)
    fifth_node = Node(5)
    insert_node = Node(6)
    seventh_node = Node(7)
    eighth_node = Node(8)
    ninth_node = Node(9)
    print(first_node)
    ll.push_front(first_node)
    print(ll)
    ll.push_front(second_node)
    print(ll)
    ll.push_front(third_node)
    print(ll)
    # print(ll.size())
    # print(ll.is_empty())
    print(ll.value_at(2))
    print(ll.pop_front())
    print(ll)
    print(ll.push_back(fourth_node))
    print(ll)
    print(ll.pop_back())
    print(ll)
    print(ll.front())
    ll.push_back(fifth_node)
    print(ll.back())
    print(ll)
    ll.insert(1,insert_node)
    print(ll)
    print(ll.insert(2, seventh_node))
    print(ll)
    print(ll.erase(1))
    print(ll)
    print(ll.remove_value(5))
    print(ll)
    print(ll.reverse())
    print(ll)
    ll.push_back(eighth_node)
    ll.push_back(ninth_node)
    print(ll)
    print(ll.distance_from_end(1))
    print(ll.remove_value(2))
    print(ll)


if __name__ == "__main__":
    main()
    