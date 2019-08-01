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
maximum_value = pow(2, 31)
input_way_edges = []
list_way_edges = {}
distance = {}
distance2 = {}
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
    distance2[i] = [maximum_value]

'''
for i in input_vertex[0:]:
    distance[i].extend([5])

distance['A'].sort()

print distance['A'][1]
'''

distance['A'] = 0
distance2['A'] = [0]
input_num_edges = input()
# priority_Queue[distance] = 0
for i in range(input_num_edges):
    input_data = raw_input().split(',')
    graph.insert(input_data[0], input_data[1], input_data[2])
    # input_way_edges.append(raw_input().split(','))
    # list_way_edges[(input_way_edges[i][0], input_way_edges[i][1])] = input_way_edges[i][2]

# (윗줄) 여기까지가 input data 정리

while len(priority_Queue) != 0:
    if distance[priority_Queue[0][0]] >= priority_Queue[0][1]:
        for i in range(len(input_vertex)):
            if graph.is_adjacent(priority_Queue[0][0], input_vertex[i]):
                if distance[input_vertex[i]] > min(distance[input_vertex[i]], distance[priority_Queue[0][0]] + int(graph.get_cost(priority_Queue[0][0], input_vertex[i]))):
                    distance[input_vertex[i]] = min(distance[input_vertex[i]], distance[priority_Queue[0][0]] + int(graph.get_cost(priority_Queue[0][0], input_vertex[i])))
                    distance2[input_vertex[i]].extend([min(distance[input_vertex[i]], distance[priority_Queue[0][0]] + int(graph.get_cost(priority_Queue[0][0], input_vertex[i])))])
                    priority_Queue.append([input_vertex[i], distance[input_vertex[i]], priority_Queue[0][0]])
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

# for i in range(len(p_distance)):
#    print p_distance[i][1]

print distance2

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
