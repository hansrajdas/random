import collections

class Graph:
    def __init__(self):
        self.g = collections.defaultdict(list)

    def add_edge(self, s, e):
        self.g[s].append(e)

    def dfs_util(self, s, visited):
        print(s)
        visited.add(s)
        for n in self.g[s]:
            if n not in visited:
                self.dfs_util(n, visited)

    def dfs(self, s):
        visited = set()
        self.dfs_util(s, visited)

g = Graph()
g.add_edge(10, 11)
g.add_edge(10, 12)
g.add_edge(11, 13)
g.add_edge(13, 14)
g.add_edge(15, 16)

# This gives 10, 11, 13, 14, 12.
# Note that 15, 16 is not reachable from 10 so these 2 vertexes will not be
# printed.
g.dfs(10)
