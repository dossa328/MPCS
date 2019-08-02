# -*- coding: utf-8 -*-
# (up line) use utf-8 coding
from Graph import Graph
graph = Graph(undirected=False)
# input
# Line 1: Names of Vertexes, separated by comma(,)
# ex) A,B,C,D,E,F,G
# Line 2: the number of edges
# Line 3~: an Edge (vertex_from, vertex_to, weight)

# output
# Line 1: shortest path distance from A to A
# Line 2: shortest path distance from A to B
# Line 3: shortest path distance from A to C
# --------------------------------------------------------
# a = list()
# a.append(t_list)
# list = ('A', 'B', 10), ('A', 'C', 5)
'''
input example
--------------
A,B,C,D,E
10
A,B,10
A,C,5
B,C,2
B,D,1
C,B,3
C,D,9
C,E,2
D,E,4
E,A,7
E,D,6
'''
target_path = []
set_path = {}
maximum_value = pow(2, 31)
input_way_edges = []
list_way_edges = {}
distance = {}
distance2 = {}
candidate_path = {}
f_candidate_path = {}
priority_Queue = []
input_vertex = raw_input().split(',')

for i in input_vertex[0:]:
    priority_Queue.append([i, maximum_value, 'x'])

for i in range(0, len(priority_Queue)):
    for j in range(0, 3):
        if priority_Queue[i][j] == 'A':
            priority_Queue[i][j+1] = 0


for i in input_vertex[0:]:
    distance[i] = maximum_value
    distance2[i] = []
    candidate_path[i] = []
    # distance2[i] = [maximum_value]

'''
for i in input_vertex[0:]:
    distance[i].extend([5])

distance['A'].sort()

print distance['A'][1]
'''

distance['A'] = 0
distance2['A'] = [0]
candidate_path = {}
input_num_edges = input()
# priority_Queue[distance] = 0
for i in range(input_num_edges):
    input_data = raw_input().split(',')
    graph.insert(input_data[0], input_data[1], input_data[2])
    # input_way_edges.append(raw_input().split(','))
    # list_way_edges[(input_way_edges[i][0], input_way_edges[i][1])] = input_way_edges[i][2]

# (윗줄) 여기까지가 input data 정리


def find_path2(input_v):
    target_path.insert(0, f_candidate_path[input_v][0])

    if f_candidate_path[input_v][0] == 'A':
        return target_path

    return find_path2(f_candidate_path[input_v][0])
    # candidate_path[start_v][0]


def make_path(sv):
    find_path2(sv)
    target_path.append(sv)
    return target_path


while len(priority_Queue) != 0:
    if distance[priority_Queue[0][0]] >= priority_Queue[0][1]:
        # input_vertex
        for i in range(len(input_vertex)):
            f_candidate_path = {}
            if graph.is_adjacent(priority_Queue[0][0], input_vertex[i]):
                if distance[input_vertex[i]] > min(distance[input_vertex[i]], distance[priority_Queue[0][0]] + int(graph.get_cost(priority_Queue[0][0], input_vertex[i]))):
                    distance[input_vertex[i]] = min(distance[input_vertex[i]], distance[priority_Queue[0][0]] + int(graph.get_cost(priority_Queue[0][0], input_vertex[i])))
                    distance2[input_vertex[i]].append(min(distance[input_vertex[i]], distance[priority_Queue[0][0]] + int(graph.get_cost(priority_Queue[0][0], input_vertex[i]))))
                    # distance2[input_vertex[i]] = ([min(distance[input_vertex[i]], distance[priority_Queue[0][0]] + int(graph.get_cost(priority_Queue[0][0], input_vertex[i])))])
                    last_weight = min(distance[input_vertex[i]], distance[priority_Queue[0][0]] + int(graph.get_cost(priority_Queue[0][0], input_vertex[i])))
                    priority_Queue.append([input_vertex[i], distance[input_vertex[i]], priority_Queue[0][0]])

                    f_candidate_path[input_vertex[i]] = [priority_Queue[0][0], input_vertex[i], last_weight]
                    # candidate_path[priority_Queue[0][0], input_vertex[i]] = distance2[input_vertex[i]]

                    candidate_path[tuple(make_path(input_vertex[i]))] = last_weight
                    # candidate_path[tuple(make_path(priority_Queue[0][0]))] = last_weight
                    target_path = []
                    # distance2[input_vertex[i]].pop()

                    # set_path[input_vertex[i]] = {candidate_path[input_vertex[i]]}
                    # candidate_path[input_vertex[i]] = {}
                    # candidate_path[input_vertex[i]][priority_Queue[0][0]] = distance2[input_vertex[i]]

#                    candidate_path[input_vertex[i]][distance2[input_vertex[i]]] = {}
#                    candidate_path[input_vertex[i]][distance2[input_vertex[i]][0]].extend([priority_Queue[0][2]])
#                    candidate_path[input_vertex[i]][distance2[input_vertex[i][0]]].extend([priority_Queue[0][0]])
                    distance2[input_vertex[i]].sort()
# distance[input_vertex[i]].sort()
        del priority_Queue[0]
        # priority_Queue.sort()
        priority_Queue = sorted(priority_Queue, key=lambda val: val[1])
    else:
        del priority_Queue[0]
        priority_Queue = sorted(priority_Queue, key=lambda val: val[1])

# print sorted(distance, key=lambda t: t[1])
p_distance = sorted(distance.items())
# find_path1 : path 역 트래킹 & 방문한 모든 vertex 반환.


'''
start_v = 'E'
print make_path(start_v)

print sorted(target_path), "cost : ", candidate_path['E'][2]

print distance2
'''

'''
k_distance = sorted(distance2.items())
for i in range(len(k_distance)):
    print k_distance[i]
'''


'''
if distance['A'] >= priority_Queue[0][1]:
    # distance['B'] = min(distance['B'], distance['A'] + graph.get_cost('A', 'B'))
    if distance['B'] > min(distance['B'], distance['A'] + int(graph.get_cost('A', 'B'))):
        distance['B'] = min(distance['B'], distance['A'] + int(graph.get_cost('A', 'B')))
        priority_Queue.append(['B', distance['B'], 'A'])
        priority_Queue.sort()
        del priority_Queue[0]
'''
#    distance['C'] = min(distance['C'], distance['A'] + graph.get_cost('A', 'C'))

# input_lists = [1, 16, 4, 10, 14, 7, 9, 3, 2, 8]
# print (sorted(priority_Queue.items(), key=lambda t: t[1]))

# print priority_Queue

# print(graph.get_cost('A', 'E'))
# print(graph.cost_matrix)
