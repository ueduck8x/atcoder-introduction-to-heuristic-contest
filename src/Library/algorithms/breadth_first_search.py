from collections import deque

from Library import Graph


def breadth_first_search(graph: Graph):
    # 距離を記録
    dist = {v: -1 for v in range(len(graph))}
    # 初期化
    dist[0] = 0
    queue = deque([0])
    # 処理
    while queue:
        v = queue.popleft()
        for e in graph.getAdjecencyList(v):
            next_node = e.end_node
            if dist[next_node] != -1:
                continue
            dist[next_node] = dist[v] + 1
            queue.append(next_node)
    return dist
