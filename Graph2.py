class Graph2:
    def __init__(self, undirected):
        self.undirected = undirected
        self.remake_graph = {}

    def insert(self, v_from, v_to, cost):

        if v_from not in self.remake_graph:
            self.remake_graph[v_from] = {}

        self.remake_graph[v_from][v_to] = cost

        if self.undirected:
            v_from, v_to = v_to, v_from
            if v_from not in self.remake_graph:
                self.remake_graph[v_from] = {}

            self.remake_graph[v_from][v_to] = cost

    def is_adjacent(self, v_from, v_to):
        if v_from not in self.remake_graph:
            return False
        elif v_to not in self.remake_graph[v_from]:
            return False
        else:
            return True

    def get_cost(self, v_from, v_to):
        if v_from not in self.remake_graph:
            raise LookupError
        elif v_to not in self.remake_graph[v_from]:
            raise LookupError
        return self.remake_graph[v_from][v_to]
