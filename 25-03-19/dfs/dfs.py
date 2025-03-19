import sys
sys.stdin = open('graph.txt', 'r')
sys.stdout = open('output.txt', 'w')

def dfs(node):

    print(node, end=' ')

    # 현재 노드에서 인접한 노드들을 모두 확인하면서, 한 군데로 진행
    for next_node in graph_list[node]:

        if visited[next_node]:
            continue

        visited[next_node] = 1

        dfs(next_node)

N, M = map(int, input().split())
# 1. 그래프를 저장하기
#   - 비어있는 그래프를 생성한다.
#   - 그래프 정보를 입력받아 넣는다.

graph_matrix = [[0] * N for _ in range(N + 1)]  # 인접 행렬
graph_list = [[] * N for _ in range(N + 1)]  # 인접 리스트

for _ in range(M):
    s, e = map(int, input().split())
    graph_list[s].append(e)
    graph_list[e].append(s)  # 양방향이라면, 뒤집어서도 저장해야한다.

visited = [0] * (N + 1)
visited[1] = 1
dfs(1)


