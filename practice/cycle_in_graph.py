import collections

class Graph:
    def __init__(self):
        self.g = {}

    def add_edge(self, start, end):
        if start in self.g:
            self.g[start].append(end)
        else:
            self.g[start] = [end]

    def check_cycle(self):
        for v in self.g:
            seen = set()
            if self.has_cycle_vertex(v, seen):
                print('Graph has cycle, ancestor vertex: %d' % v)
                return True
        return False

    def has_cycle_vertex(self, v, seen):
        seen.add(v)
        for adj in self.g.get(v, []):
            if adj in seen:
                return True
            return self.has_cycle_vertex(adj, seen)


g1 = Graph()
g1.add_edge(10, 11)
g1.add_edge(10, 12)
g1.add_edge(11, 13)
g1.add_edge(13, 14)
g1.add_edge(15, 15)

assert g1.check_cycle() == True
