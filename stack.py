from __future__ import annotations
from typing import Any

class EmptyStackError(Exception):
    def __str__(self) -> str:
        return 'you loser, you tried to pop an empty stack'

#python doesn't inforce public and private variables but other lanuages do
#accessing private variables outside of class is bad form


#can't iterate through your own stack
class Stack:
    _items: list[Any]  # means any data type

    # difference between object and Any:

    def __init__(self) -> None:
        self._items = []

    def push(self, item: object) -> None:
        self._items.append(item)

    def pop(self) -> object:
        if not self.is_empty():
            return self._items.pop()
        raise EmptyStackError

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def copy(self) -> Stack:
        count = 0
        s = Stack()
        while count != len(self._items) - 1:
            s.push(self._items[count])
            count += 1
        return s


class BackStack:
    _lst: list[Any]

    def __init__(self):
        self._lst = []

    def enqueue(self, value) -> None:
        self._lst.insert(0, value)

    def dequeue(self) -> None:
        return self._lst.pop(0)

    def is_empty(self) -> bool:
        return len(self._lst) == 0

    def peek(self) -> None:
        if self.is_empty():
            raise EmptyStackError
        return self._lst[-1]


def size(s: Stack) -> int:
    s2 = Stack()
    count = 0
    while not s.is_empty():
        count +=1
        s2.push(s.pop())

    while not s2.is_empty():
        s.push(s2.pop())

def is_balanced(line: str) -> bool:
    tracker = {')': '(', "}": '{', "]": '['}
    stack = Stack()
    for char in line:#({[]})
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if not stack.is_empty() and stack.pop() == tracker[char]:
                continue
            else:
                return False

    if stack.is_empty():
        return True
    return False