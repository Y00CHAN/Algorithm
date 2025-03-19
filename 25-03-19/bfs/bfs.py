import sys
sys.stdin = open('graph.txt', 'r')
sys.stdout = open('output.txt', 'w')

def bfs(start_node):
    # q에 들어가는 노드들의 의미 : 다음에 방문해야 할 노드들(대기열)
    q = [start_node]  # 시작점을 넣은 상태로 출발

    while q:
        # 1. 가장 앞에 있는 노드를 뽑는다.
        # 2. 해당 노드에서 갈 수 있는 노드들을 queqe에 넣는다.
        now = q.pop(0)

        print(now, end=' ')

        for next_node in graph_list[now]:
            if visited[next_node]:
                continue

            visited[next_node] = 1
            q.append(next_node)

N, M = map(int, input().split())

graph_matrix = [[0] * N for _ in range(N + 1)]
graph_list = [[] * N for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph_list[s].append(e)
    graph_list[e].append(s)

visited = [0] * (N + 1)
visited[1] = 1
bfs(1)



