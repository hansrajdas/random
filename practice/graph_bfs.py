import collections

class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def bfs(self, start):
        queue = collections.deque()
        queue.append(start)
        visited = set()
        while queue:
            node = queue.popleft()
            print(node)
            visited.add(node)
            for n in self.graph[node]:
                if n not in visited:
                    queue.append(n)
                    visited.add(n)
g = Graph()

g.add_edge(10, 11)
g.add_edge(10, 12)
g.add_edge(11, 12)
g.add_edge(12, 10)
g.add_edge(12, 13)
g.add_edge(13, 12)
g.add_edge(13, 14)
g.add_edge(13, 13)

g.bfs(13)
