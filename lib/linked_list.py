from lib.node import Node

class LinkedList:
    """Represents a linked list."""

    def __init__(self):
        """Initializes an empty linked list."""
        self.head = None

    def append(self, data):
        """Appends a new node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_node

    def insert(self, index, data):
        """Inserts a new node with the given data at the specified index."""
        if index < 0 or index > self.length():
            raise IndexError("Index out of range")

        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node

    def length(self):
        """Returns the length of the linked list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count