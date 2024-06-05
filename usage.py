from arrays import Array
from stack import Stack
from my_queue import Queue
from doubly_linked_list import DoublyLinkedList, Node
from hash_table import HashTable
from binary_search_tree import BinarySearchTree

# Example usage of Array
array = Array(5)
array.append(1)
array.append(2)
array.append(3)
print("Array:", array.display(), "\n")

# Example usage of LinkedList
dll = DoublyLinkedList()
head = Node(1)
dll.insert(head)
dll.insert(Node(4))
dll.insert(Node(9))
dll.insert(Node(16))

print("Linked list: ", dll.display())

dll.insert(Node(25))

print("After insertion:", dll.display())

dll.delete(head)

print("After deletion:", dll.display(), "\n")

# Example usage of Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack.display(), "\n")

# Example usage of Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue:", queue.display(), "\n")

# Example usage of Hash Table
hash_table = HashTable(10)
hash_table.insert('key1', 'value1')
hash_table.insert('key2', 'value2')
print("HashTable:", hash_table.display(), "\n")

# Example usage of Binary Search Tree
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("BST Inorder traversal:", bst.inorder_traversal())

bst.delete(20)
print("After deleting 20:", bst.inorder_traversal())

bst.delete(30)
print("After deleting 30:", bst.inorder_traversal())

bst.delete(50)
print("After deleting 50:", bst.inorder_traversal())