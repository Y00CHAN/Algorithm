import heapq
import sys
sys.stdin = open('graph.txt', 'r')
sys.stdout = open('output.txt', 'w')

def prim(start_node):
    pq = [(0, start_node)]  # 시작점 가중치 0
    MST = [0] * V  # visited
    min_weight = 0

    while pq:
        weight, node = heapq.heappop(pq)

        if MST[node]:
            continue

        MST[node] = 1
        min_weight += weight

        for next_node in range(V):
            if graph[node][next_node] == 0:
                continue

            if MST[next_node]:
                continue

            heapq.heappush(pq, (graph[node][next_node], next_node))

    return min_weight

V, E = map(int, input().split())
graph = [[0] * V for _ in range(V + 1)]

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight
    graph[end][start] = weight

result = prim(0)
print(result)




