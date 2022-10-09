class Node:
    def __init__(self, data, arbitrary=None, next=None):
        self.data = data
        self.next: Node = next
        self.arbitrary: Node = arbitrary


class LinkedList:
    def __init__(self, head=None):
        self.head: Node = head

    def append(self, data: int) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node


def deep_copy_arbitrary_pointer(head: LinkedList) -> LinkedList:
    head_node: Node = None
    copied_list: LinkedList = None
    already_existed_node: dict = {}
    current_node: Node = None

    while head.head.next:
        if head_node is None:
            head_node = head.head
            copied_list.head = Node(head_node.data)
            already_existed_node[copied_list.head.data] = copied_list.head

            copied_list.head.next = Node(head_node.next.data)
            already_existed_node[copied_list.head.next.data] = copied_list.head.next

            copied_list.head.arbitrary = Node(head_node.arbitrary.data)
            already_existed_node[copied_list.head.arbitrary.data] = copied_list.head.arbitrary

            current_node = copied_list.head
        else:
            while head_node.next:
                head_node = head_node.next
                print(head_node.data)




    return None


if __name__ == "__main__":
    head = LinkedList()
    for i in [4, 8, 15, 19]:
        head.append(i)

    deep_copy_arbitrary_pointer(head)
