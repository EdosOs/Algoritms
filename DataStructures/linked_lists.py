'''
A list that does not take continues place in memory and can't be
referenced numerically, rather connected by pointers which point to
the next node in the list.

singly linked list:
starts with a head , every node has a single pointer pointing to the
next node except for the tail which points to null.

complexity:
search : O(n)
adding a node at head O(1)
adding a node at tail O(1)
remove at head O(1)
removing at tail O(n)* - if we want to keep track of tail value we must go through the entire list to get it's new value.
doubly linked list:
similar to a singly but each node has 2 pointers one for each neighbour
complexity:
search : O(n)
adding a node at head O(1)
adding a node at tail O(1)
remove at head O(1)
removing at middle O(n)
removing at tail O(1)
'''
class SinglyLinkedList():
    pass

class DoublyLinkedList():
    pass