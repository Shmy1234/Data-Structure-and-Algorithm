from __future__ import annotations
from typing import Any, Optional


class BST:
    root: Optional[Any]
    left: Optional[Any]
    right: Optional[Any]

    def __init__(self, root) -> None:
        self.root = None
        if root is not None:
            self.left = None
            self.right = None
        else:
            self.left = BST(None)
            self.right = BST(None)

    def is_empty(self) -> bool:
        return self.root is None

    def insert(self, item: Any) -> None:
        pass

    def delete(self, item: Any) -> None:
        if self.is_empty():
            pass # can't remove from an empty tree
        elif self.root == item:
            self.delete_root()
        elif self.root < item:
            self.left.delete(item)
        elif self.root > item:
            self.right.delete(item)

    def delete_root(self) -> None:
        if self.left.is_empty() and self.right.is_empty():
            self.root = None
            self.left = None
            self.right = None
        elif self.left.is_empty():
            self.root = self.right.root
            self.left = self.right.left
            self.right = self.right.right
        elif self.right.is_empty():
            self.root = self.left.root
            self.left = self.left.left
            self.right = self.left.right
        else:
            self.root = self.right.extract_min() # or self.left.extract_max()

    def format(self, lst: list): #pre-order
        if self.is_empty():
            return None

        if not self.left.is_empty(): #recurse through left
            self.left.format(lst)

        if not self.right.is_empty(): #recurse through right
            self.right.format(lst)


        lst.append(self.root)  # proccess the root












