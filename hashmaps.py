from __future__ import annotations
from typing import Any

class HashMap:
    Max: int
    lst: list[Any]
    
    def __init__(self):
        self.Max = 100
        self.lst = [None for i in range(self.Max)]

    def get_hash(self, key: Any) -> int:
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max

    def __setitem__(self, key: Any, value: Any) -> None:
        h = self.get_hash(key)
        self.lst[h] = value

    def __getitem__(self, key: int) -> Any:
        h = self.get_hash(key)
        return self.lst[h]

    def __delitem__(self, key: int) -> None:
        h = self.get_hash(key)
        self.lst[h] = None

class CollisionHashMap:
    Max: int
    lst: list[Any]

    def __init__(self):
        self.Max = 100
        self.lst = [None for i in range(self.Max)]

    def get_hash(self, key: Any) -> int: #Popular hash function
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max

    def __setitem__(self, key: Any, value: Any) -> None:
        h = self.get_hash(key)
        found = False

        for idx, elem in enumerate(self.lst[h]):
            if elem == 2 and elem[0] == key:
                self.lst[h][idx] = (key, value)
                found = True
                break

        if not found:
            self.lst[h].append((key,value))

    def __getitem__(self, key: int) -> Any:
        h = self.get_hash(key)
        for item in self.lst[h]:
            if item[0] == key:
                return item[1]

        raise ValueError

    def __delitem__(self, key: int) -> None:
        h = self.get_hash(key)
        for inx, elem in enumerate(self.lst[h]):
            if elem[0] == key:
                del self.lst[h][inx]

