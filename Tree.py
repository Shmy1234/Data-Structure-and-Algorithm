from __future__ import annotations

from typing import Any, Optional, Union, Callable


class Tree:
    root: Optional[Any]
    subtrees: list[Tree]

    def __init__(self, root: Optional[Any], subtrees: list[Tree]) -> None:
        self.root = root
        self.subtrees = subtrees

    def is_empty(self) -> bool:
        return not self.subtrees and not self.root

    def to_nested_list(self) -> list[int]:
        if self.is_empty():
            return []
        elif self.subtrees == []:
            return [self.root]
        else:
            res = [self.root]
            for subtree in self.subtrees:
                res.append(subtree.to_nested_list())
            return res

    def pre_order_visit(self, act: Callable[[Any], Any]) -> None:
        if self.is_empty():
            return None
        act(self.root)
        for subtree in self.subtrees:
            subtree.pre_order_visit(act)

    def post_order_visit(self, act: Callable[[Any], Any]) -> None:
        if self.is_empty():
            return None
        elif self.subtrees == []:
            act(self.root)
        else:
            for subtree in self.subtrees:
                subtree.post_order_visit(act)

    def level_order_visit(self, act: Callable[[Any], Any]) -> None:
        if self.is_empty():
            return []
        else:
            lst = [self]
            while lst:
                c = lst.pop(0)
                print(c.root)
                lst.extend(c.subtrees)

    def width(self) -> None:
        if self.is_empty():
            return 0
        else:
            lst = [self]
            max_w = 0
            while lst:
                cur_w = len(lst)
                max_w = max(max_w, cur_w)
                for i in range(cur_w):
                    curr_tree = lst.pop(0)
                    lst.extend(curr_tree.subtrees)


def operation(t: Tree) -> None:
    print(t.root)


def to_tree(obj: Union[int, list]) -> Optional[Tree]:
    if obj == []:
        return Tree(None, [])
    elif isinstance(obj, int):
        return None
    else:
        t = obj.copy()
        root = t.pop(0)
        lst = []
        if isinstance(root, list):
            return None
        for subtree in obj[1:]:
            s = to_tree(subtree)
            if s is None:
                return None
            lst.append(s)

        return Tree(root, lst)
