from typing import Any


class Graph:
    edgeList: list[tuple[Any, Any]]
    AjList: dict[str, str]
    def __init__(self, edges: list[tuple[Any, Any]]) -> None:
        self.edgeList = edges
        self.AjList = {}
        for edge in edges:
            self.AjList[edge[0]] = [edge[1]] + self.AjList.get(edge[1], [])

    def get_path(self, start: Any, end: Any, path: list[Any] = []) -> list[Any]:
        path = path + [start]
        if start == end:
            return path
        elif start not in self.AjList:
            return []
        else:
            path = []
            for node in self.AjList[start]:
                if node not in path:
                    new_paths = path.get_path(node, end, path)
                    for new_path in new_paths:
                        path.append(new_path)

            return path

    def shortest_path(self, start: Any, end: Any, path: list[Any] = []) -> list[Any]:
        path = path + [start]
        if start == end:
            return path
        elif start not in self.AjList:
            return []
        else:
            shortestPath = []
            for node in self.AjList[start]:
                shortestPath2 = self.shortest_path(node, end, path)
                if shortestPath==[] or len(shortestPath2) < len(shortestPath):
                    shortestPath = shortestPath2

            return shortestPath






