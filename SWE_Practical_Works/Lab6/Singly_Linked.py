class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
class LinkedList:
    # ... (previous code)

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# Test the append method
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
class LinkedList:
    # ... (previous code)

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

# Test the display method
ll.display()  # Output: 1 -> 2 -> 3
class LinkedList:
    # ... (previous code)

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

# Test the insert method
ll.insert(4, 1)
ll.display()  # Output: 1 -> 4 -> 2 -> 3
class LinkedList:
    # ... (previous code)

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

# Test the delete method
ll.delete(2)
ll.display()  # Output: 1 -> 4 -> 3
class LinkedList:
    # ... (previous code)

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

# Test the search method
print(ll.search(4))  # Output: 1
print(ll.search(5))  # Output: -1
class LinkedList:
    # ... (previous code)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Test the reverse method
ll.reverse()
ll.display()  # Output: 3 -> 4 -> 1
