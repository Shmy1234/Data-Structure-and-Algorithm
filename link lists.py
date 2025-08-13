from __future__ import annotations

from typing import Any, Union


class Node:
    data: Any

    def __init__(self, data: Any, next: Node = None):
        self.data = data
        self.next = next


class LinkedList:
    head: Union[Node, None]
    len: int

    def __init__(self, head: Any = None):  # initalizer
        self.head = head
        self.len = 0

    def __str__(self):
        lst = []
        node = self.head
        while node:
            lst.append(node.data)
            node = node.next
        return str(lst)

    def __eq__(self, other: LinkedList) -> bool:
        if self.length() != other.length():
            return False
        node1 = self.head
        node2 = other.head
        while node1 and node2:
            if node1.data != node2.data:
                return False
            node1 = node1.next
            node2 = node2.next

        return True

    def __getitem__(self, index: Union[int, slice]) -> Union[Any, LinkedList]:
        node = self.head
        step = 0
        count = 0
        if index.start > self.__len__() or index.stop > self.__len__():
            raise IndexError

        elif isinstance(index, int):
            while node:
                if count == index:
                    return node.data
                count += 1
                node = node.next
        else:
            lst = []
            while node:
                if index.start <= count <= index.stop:
                    step += 1
                    if step % index.step == 0:
                        lst.append(node)
                count += 1
                node = node.next
            return lst

    def __setitem__(self, index: int, value: Any) -> None:
        node = self.head
        count = 0
        while node:
            if count == index:
                node.data = value
            count += 1
            node = node.next

    def __len__(self) -> int:
        return self.len

    def insert(self, data: Any, index: int) -> None:
        new_node = Node(data)
        if index > self.__len__():
            raise IndexError
        elif index == 0:
            self.head, new_node.next = new_node, self.head
        else:
            # Iterate to (index-1)-th node.
            curr = self.head
            count = 0
            while (index > 0 and count < index - 1) or (index < 0 and count < count - index):
                curr = curr.next
                count += 1

            curr.next, new_node.next = new_node, curr.next

    def pop(self) -> int:  # delete last node from the list
        if self.head:
            prev = self.head
            node = self.head.next
            if not node:
                self.head = None
                return self.head.data
            else:
                while node:
                    if not node.next:
                        prev.next = None
                        self.len -= 1
                        return node.data
                    prev = node
                    node = node.next

        raise ValueError('Linked List is empty')

    def push(self, item: Any) -> None:  # add node to first position
        new_head = Node(item, self.head)
        self.head = new_head
        self.len += 1

    def enqueue(self, item: Any) -> None:  # add node to last position
        new_tail = Node(item)
        node = self.head
        if node is None:
            self.head = new_tail
            self.len += 1
        elif node.next:
            node.next = new_tail
        else:
            while node.next:
                node = node.next
            node.next = new_tail
            self.len += 1

    def dequeue(self) -> None:  # delete first node
        self.head = self.head.next
        self.len -= 1

    def remove(self, data: Any) -> None:  # remove first node with the data
        found = False
        if not self.head:
            raise ValueError("Linked List is empty")
        elif self.head.data == data:
            self.head = self.head.next
            self.len -= 1
            found = True
        else:
            node = self.head
            node_next = node.next

            while node_next:
                if node_next.data == data:
                    node.next = node_next.next
                    found = True
                    self.len -= 1
                    break
                node, node_next = node_next, node_next.next

        if not found:
            raise ValueError("No Node with value " + str(data))

    def remove_all(self, data: Any) -> None:  # remove all nodes that have the data value
        node = self.head
        while node:
            if node.data == data:
                self.remove(node.data)
                self.len -= 1
            node = node.next

    def contains(self, item: Any) -> bool:  # True if linked list has item
        node = self.head
        while node:
            if node.data == item:
                return True
            node = node.next
        return False

    def count(self, item: Any) -> int:  # counts number of time a node has the data
        count = 0
        node = self.head
        while node:
            if node.data == item:
                count += 1
            node = node.next
        return count

    def index(self, item: Any) -> int:  # returns position of first appearance of data value
        node = self.head
        count = 0
        while node:
            if node.data == item:
                return count
            node = node.next
            count += 1
        return count

    def length(self) -> int:  # O(n) version of finding the length
        node = self.head
        count = 0
        while node:
            node = node.next
            count += 1
        return count

    def right_index(self, item: Any) -> int:  # returns position of last appearance of data value
        node = self.head
        count = 0
        indexes = []
        while node:
            if node.data == item:
                indexes.append(count)
            node = node.next
            count += 1

        return indexes.pop()