from __future__ import annotations
from typing import Any

class Node:
    data: Any
    
    def __init__(self, data: Any, next: Node = None, prev: Node = None):
        self.data = data
        self.prev = prev
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    head: Optional[Node]
    tail: Optional[Node]
    
    def __init__(self, head: Any = None, tail: Any = None): #initalizer
        self.head = head
        self.tail = tail


    def __str__(self):
        lst = []
        node = self.head
        while node is not None:
            lst.append(node.data)
            node = node.next
        return str(lst)

    def __eq__(self, other: DoubleLinkedList) -> bool:
        if self.length() != other.length():
            return False
        node1 = self.head
        node2 = other.head
        while node1 is not None:
            if node1.data != node2.data:
                return False
            node1 = node1.next
            node2 = node2.next

        return True

    def __getitem__(self, index: int) -> Any:
        node = self.head
        count = 0
        while node is not None:
            if count == index:
                return node.data
            count += 1
            node = node.next
        raise IndexError

    def __setitem__(self, index: int, value: Any) -> None:
        node = self.head
        count = 0
        while node is not None:
            if count == index:
                node.data = value
            count += 1
            node = node.next

    def insert(self, data: Any, index: int) -> None:
        if index > self.length() or index < 0:
            raise IndexError
        elif index == 0:
            self.head = Node(data, self.head)

        node = self.head
        count = 0

        while node is not None:
            if count + 1 == index:
                node.next = Node(data, node.next, node)
            node = node.next
            count += 1

    def pop(self) -> None: #delete last node from the list
        if self.tail is not None:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            raise ValueError('No tail')


    def push(self, item: Any) -> None: #add node to first position
        new_head = Node(item, self.head, None)
        self.head.prev, self.head = new_head, new_head

    def enqueue(self, item: Any) -> None: #add node to last position
        new_tail = Node(item)
        node = self.head
        if node.next is None:
            node.next = new_tail
        else:
            while node.next is not None:
                node = node.next
            node.next = Node(item, None, node)
            self.tail = node.next

    def dequeue(self) -> None: #delete first node from the list
        self.head = self.head.next
        self.head.prev = None

    def remove(self, data: Any) -> None:
        found = False
        if self.head is None:
            raise ValueError("Linked List is empty")
        elif self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            found = True
        else:
            node = self.head
            node_next = node.next

            while node_next is not None:
                if node_next.data == data:
                    node.next, node_next.next.prev = node_next.next, node
                    found = True
                    break
                node, node_next = node_next, node_next.next

        if not found:
            raise ValueError("No Node with value " + str(data))


    def length(self) -> int: #length of linked list
        node = self.head
        count = 0
        while node is not None:
            node = node.next
            count += 1
        return count

    def contains(self, item: Any) -> bool: #True if linked list has item
        node = self.head
        while node is not None:
            if node.data == item:
                return True
            node = node.next
        return False