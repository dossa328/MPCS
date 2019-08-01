# -*- coding: utf-8 -*-
from Graph import Graph
graph = Graph(undirected=False)

# Graph 입력 및 Graph 생성 (dic 형태)
# input(S,E) 에 대해서 Dijkstra 구함
# 최단 경로 가중치 w(s,e) 까지는 구해진거임.
# Candidate path 를 구해야함. 어떻게?
# 출력된 각 최단 경로 가중치에 + 알파값을 한 다음 그것보다 작은 "여러개"의 candidate path set이 나오면됨
# 여기서 알파값은 1보다 크거나 같아야함.

def candidate_path():
