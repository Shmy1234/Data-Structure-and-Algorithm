from __future__ import annotations
from typing import Any

class EmptyStackError(Exception):
    def __str__(self) -> str:
        return 'stack is empty'

class Queue:
    _lst: list[Any]
    head: Any
    tail: Any

    def __init__(self):
        self._lst = []
        self._head = None
        self._tail = None

    def enqueue(self, value) -> None:
        self._lst.append(value)

    # self._lst.insert(0, value) if we set the back as the first index and front as last index

    def dequeue(self) -> None:
        if not self.lst.is_empty():
            return self._lst.pop(0)
        raise EmptyStackError

    # self._lst.pop() if we set the back as the first index and front as last index

    def is_empty(self) -> bool:
        return len(self._lst) == 0

    def peek(self) -> Any:
        return self._lst[0]