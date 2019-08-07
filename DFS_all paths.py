from Graph import Graph
from copy import deepcopy as c
graph = Graph(undirected=False)

visit = list()
stack = list()
all_path = {}
candidate_path = []
cc = 0


class Allpathweight:

    def __init__(self):
        pass

    def dfs(self, start, end, vertex):
        visit.append(start)
        stack.append(start)
        if start == end:
            all_path[start] = c(stack)
            candidate_path.extend((all_path.values()))
            stack.pop()
            return candidate_path
        for it in vertex:
            if graph.is_adjacent(start, it):
                if it not in visit:
                    dfs(it, end)
                    visit.remove(it)

        stack.pop()

    def dfs_out(self, ):
        for i in range(len(candidate_path)):
            cc = 0
            for j in range(len(candidate_path[i]) - 1):
                cc = cc + int(graph.get_cost(candidate_path[i][j], candidate_path[i][j + 1]))
            candidate_path[i].append(cc)

            return candidate_path






dfs(in_start, 'F31')