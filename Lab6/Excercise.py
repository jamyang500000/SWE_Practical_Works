class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

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

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def remove_duplicates(self):
        current = self.head
        prev = None
        seen = set()
        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next

    def merge_sorted(self, other):
        dummy = Node(0)
        tail = dummy
        a = self.head
        b = other.head

        while a and b:
            if a.data < b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        if a:
            tail.next = a
        else:
            tail.next = b

        return dummy.next

# Test the LinkedList methods
if __name__ == "__main__":
    # Create and test the linked list
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.display()  # Output: 1 -> 2 -> 3

    ll.insert(4, 1)
    ll.display()  # Output: 1 -> 4 -> 2 -> 3

    ll.delete(2)
    ll.display()  # Output: 1 -> 4 -> 3

    print(ll.search(4))  # Output: 1
    print(ll.search(5))  # Output: -1

    ll.reverse()
    ll.display()  # Output: 3 -> 4 -> 1

    print(ll.find_middle())  # Output: 4

    print(ll.has_cycle())  # Output: False

    # Creating a cycle for testing
    ll.head.next.next.next = ll.head  # Creating a cycle for testing
    print(ll.has_cycle())  # Output: True

    ll2 = LinkedList()
    ll2.append(0)
    ll2.append(2)
    ll2.append(5)

    merged_list = LinkedList()
    merged_list.head = ll.merge_sorted(ll2)
    merged_list.display()  # Output: 0 -> 1 -> 2 -> 3 -> 4 -> 5
