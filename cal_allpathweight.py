'''
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


dfs(in_start, in_end)

cc = 0
for i in range(len(candidate_path)):
    cc = 0
    for j in range(len(candidate_path[i])-1):
        cc = cc + int(graph.get_cost(candidate_path[i][j], candidate_path[i][j+1]))
    candidate_path[i].append(cc)


print candidate_path

# 경로 + 경로 w 구하기 끝
# ---------------------------------------------------------------------
'''