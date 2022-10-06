from __future__ import annotations
from tkinter import W

class Node:
    def __init__(self, data: int, next_node:Node = None) -> None:
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, data: int)-> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def insert(self, data: int) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.insert(0)

    print(linked_list)
    print(linked_list.head.data)
    print(linked_list.head.next.data)
    print(linked_list.head.next.next.data)
    print(linked_list.head.next.next.next.data)
