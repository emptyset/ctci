class Graph:
    def __init__(self, nodes=[]):
        self._nodes = set(nodes)

    @property
    def nodes(self):
        return self._nodes

    def link(self, origin, target):
        if all(node in self._nodes for node in [origin, target]):
            origin.link(target)
        else:
            raise ValueError


class Node:
    def __init__(self, value, directed=False):
        self._value = value
        self._directed = directed
        self._incoming = set()
        self._outgoing = set()

    @property
    def value(self):
        return self._value

    @property
    def directed(self):
        return self._directed

    @property
    def incoming(self):
        return self._incoming

    @property
    def outgoing(self):
        return self._outgoing

    @property
    def neighbors(self):
        return self.incoming.union(self.outgoing)

    def link(self, target):
        # do not allow linking directed and undirected nodes
        if self.directed != target.directed:
            raise ValueError

        # always link source -> target
        self.outgoing.add(target)
        target.incoming.add(self)

        if not self.directed:
            # link bidirectionally, target -> source
            target.outgoing.add(self)
            self.incoming.add(target)
