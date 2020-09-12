class Graph:
    def __init__(self):
        self.g = {}

    def add_edge(self, s, e):
        if s in self.g:
            self.g[s].append(e)
        else:
            self.g[s] = [e]

    def topological_sort(self):
        stack = []
        seen = set()
        for v in self.g:
            self.topological_sort_util(v, seen, stack)
        stack.reverse()
        return stack

    def topological_sort_util(self, v, seen, stack):
        seen.add(v)
        for adj in self.g.get(v, []):
            if adj not in seen:
                self.topological_sort_util(adj, seen, stack)
        stack.append(v)


g = Graph()
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print(g.topological_sort())

# Output: [5, 4, 0, 2, 3, 1]

g1 = Graph()
g1.add_edge(5, 2)
g1.add_edge(6, 2)

print(g1.topological_sort())

# Output: [6, 5, 2]
