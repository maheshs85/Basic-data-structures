class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.dummy = Node()  # Sentinel node
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def insert(self, node):
        node.next = self.dummy.next
        self.dummy.next.prev = node
        self.dummy.next = node
        node.prev = self.dummy

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def display(self):
        current = self.dummy.next
        elements = []
        while current != self.dummy:
            elements.append(current.data)
            current = current.next
        return elements
