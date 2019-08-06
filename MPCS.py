# -*- coding: utf-8 -*-
# (up line) use utf-8 coding
from Graph import Graph
from copy import deepcopy as c
graph = Graph(undirected=False)
maximum_value = pow(2, 31)
input_way_edges = []
list_way_edges = {}
distance = {}
priority_Queue = []
distance2 = {}
input_vertex = raw_input().split(',')
for i in input_vertex[0:]:
    priority_Queue.append([i, maximum_value, 'x'])

for i in range(0, len(priority_Queue)):
    for j in range(0, 3):
        if priority_Queue[i][j] == 'A':
            priority_Queue[i][j + 1] = 0

for i in input_vertex[0:]:
    distance[i] = maximum_value

distance['E9'] = 0
distance2['E9'] = [0]
input_num_edges = input()
for i in range(input_num_edges):
    input_data = raw_input().split(',')
    graph.insert(input_data[0], input_data[1], input_data[2])

# (윗줄) 여기까지가 input data 정리
if priority_Queue[0][0] == 'A':
    priority_Queue[0][2] = 'A'

while len(priority_Queue) != 0:
    if distance[priority_Queue[0][0]] >= priority_Queue[0][1]:
        for i in range(len(input_vertex)):
            if graph.is_adjacent(priority_Queue[0][0], input_vertex[i]):
                if distance[input_vertex[i]] > min(distance[input_vertex[i]], distance[priority_Queue[0][0]] + int(graph.get_cost(priority_Queue[0][0], input_vertex[i]))):
                    distance[input_vertex[i]] = min(distance[input_vertex[i]], distance[priority_Queue[0][0]] + int(graph.get_cost(priority_Queue[0][0], input_vertex[i])))
                    priority_Queue.append([input_vertex[i], distance[input_vertex[i]], priority_Queue[0][0]])

        del priority_Queue[0]
        # priority_Queue.sort()
        priority_Queue = sorted(priority_Queue, key=lambda val: val[1])
    else:
        del priority_Queue[0]
        priority_Queue = sorted(priority_Queue, key=lambda val: val[1])


# 모든 A -> E 경로 + W 구하기
# ---------------------------------------------------------------------
visit = list()
stack = list()
all_path = {}
candidate_path = []


def dfs(start, end):
    visit.append(start)
    stack.append(start)
    if start == end:
        all_path[start] = c(stack)
        candidate_path.extend((all_path.values()))
        # print all_path
        # print("출력완료")
        stack.pop()
        return candidate_path

    for it in input_vertex:
        if graph.is_adjacent(start, it):
            if it not in visit:
                dfs(it, end)
                visit.remove(it)

    stack.pop()


dfs('A', 'E')

cc = 0
for i in range(len(candidate_path)):
    cc = 0
    for j in range(len(candidate_path[i])-1):
        cc = cc + int(graph.get_cost(candidate_path[i][j], candidate_path[i][j+1]))
    candidate_path[i].append(cc)


print candidate_path

# 경로 + 경로 w 구하기 끝
# ---------------------------------------------------------------------

# print sorted(distance, key=lambda t: t[1])


p_distance = sorted(distance.items())


for i in range(len(p_distance)):
    print p_distance[i][1]
