from typing import List


class Edge:
    def __init__(self, end_node: int, weight: int) -> None:
        self.end_node = end_node
        self.weight = weight


class Graph:
    def __init__(self, num_vertices: int):
        self.nodes: dict[int, list[Edge]] = {v: [] for v in range(num_vertices)}

    def __len__(self) -> int:
        return len(self.nodes)

    def addEdge(self, start_node: int, end_node: int, weight: int = 1) -> None:
        self.nodes[start_node].append(Edge(end_node, weight))
        self.nodes[end_node].append(Edge(start_node, weight))

    def getAdjecencyList(self, node: int) -> List[Edge]:
        return self.nodes[node]


class DiGraph(Graph):
    def __init__(self, num_vertices: int) -> None:
        super().__init__(num_vertices)

    def addEdge(self, start_node: int, end_node: int, weight: int = 1) -> None:
        self.nodes[start_node].append(Edge(end_node, weight))
