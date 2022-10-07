from __future__ import annotations

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


""""
Given two sorted linked lists, merge them so that the resulting linked list is also sorted. Consider two sorted linked lists and the merged list below them as an example.

head1 [4, 8, 15, 19] none
head2 [7, 9, 10, 16] none

head  [4, 7, 8, 9, 10, 15, 16, 19] none
"""

if __name__ == "__main__":
    head1 = LinkedList()
    head2 = LinkedList()
    for i in [4, 8, 15, 19]:
        head1.append(i)
    for i in [7, 9, 10, 16]:
        head2.append(i)

    merged_linked_list = LinkedList()

    current_head1 = head1.head
    current_head2 = head2.head

    while current_head1.next or current_head2.next:
        last_node = merged_linked_list.head

        if merged_linked_list.head is None:
            if current_head1.data < current_head2.data:
                merged_linked_list.head = Node(current_head1.data)
                current_head1 = head1.head.next
            else:
                merged_linked_list.head = Node(current_head2.data)
                current_head2 = head2.head.next
        else:
            while last_node.next:
                last_node = last_node.next

            if current_head1.data < current_head2.data:
                last_node.next = Node(current_head1.data)
                current_head1 = current_head1.next
            else:
                last_node.next = Node(current_head2.data)
                current_head2 = current_head2.next

    while last_node.next:
        last_node = last_node.next

    if current_head1.data < current_head2.data:
        last_node.next = Node(current_head1.data)
        last_node.next.next = Node(current_head2.data)
    else:
        last_node.next = Node(current_head2.data)
        last_node.next.next = Node(current_head1.data)

    print(merged_linked_list.head.data)
    print(merged_linked_list.head.next.data)
    print(merged_linked_list.head.next.next.data)
    print(merged_linked_list.head.next.next.next.data)
    print(merged_linked_list.head.next.next.next.next.data)
    print(merged_linked_list.head.next.next.next.next.next.data)
    print(merged_linked_list.head.next.next.next.next.next.next.data)
    print(merged_linked_list.head.next.next.next.next.next.next.next.data)
