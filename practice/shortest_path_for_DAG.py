class Graph:
    def __init__(self):
        self.g = {}
        self.dist = {}

    def add_edge(self, u, v, w):
        if u in self.g:
            self.g[u].append((v, w))
        else:
            self.g[u] = [(v, w)]
        self.dist[u] = float('Inf')
        self.dist[v] = float('Inf')

    def shortest_path(self, s):
        if s not in self.g:
            print('Not outgoing edge from %d' % s)
            return None
        stack = []
        seen = set()

        self._topological_sort(s, stack, seen)

        stack.reverse()
        self.dist[s] = 0

        for u in stack:
            for v, w in self.g.get(u, []):
                self.dist[v] = min(self.dist[u] + w, self.dist[v])

        print('Source: %d' % s)
        for u in self.dist:
            print('Vertex: %d, Distance: %s' % (u, self.dist[u]))

    def _topological_sort(self, u, stack, seen):
        seen.add(u)
        for v, w in self.g.get(u, []):
            if v not in seen:
                self._topological_sort(v, stack, seen)
        stack.append(u)


g = Graph()
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 4)
g.add_edge(2, 3, 4)
g.add_edge(4, 3, 4)
g.add_edge(5, 3, 4)
g.shortest_path(3)
# None of the vertex is reachable from 3, so no shortest path

g.shortest_path(1)
# Vertex and distance
# Vertex: 1 Distance: 0
# Vertex: 2 Distance: 3
# Vertex: 3 Distance: 4
# Vertex: 4 Distance: inf
# Vertex: 5 Distance: inf

g = Graph()
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 3)
g.add_edge(1, 3, 6)
g.add_edge(1, 2, 2)
g.add_edge(2, 4, 4)
g.add_edge(2, 5, 2)
g.add_edge(2, 3, 7)
g.add_edge(3, 4, -1)
g.add_edge(4, 5, -2)
g.shortest_path(1)
# Vertex and distance
# Vertex: 0 Distance: inf
# Vertex: 1 Distance: 0
# Vertex: 2 Distance: 2
# Vertex: 3 Distance: 6
# Vertex: 4 Distance: 5
# Vertex: 5 Distance: 3
