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

