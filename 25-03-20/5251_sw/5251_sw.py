import sys
sys.stdin = open('sample_input (1).txt', 'r')
sys.stdout = open('output.txt', 'w')

import heapq

def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [INF] * (V + 1)
    dists[start_node] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if dists[node] < dist:
            continue

        for next_info in graph[node]:
            next_dist = next_info[0]
            next_node = next_info[1]

            new_dist = dist + next_dist

            if dists[next_node] <= new_dist:
                continue

            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return dists


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    INF = float('inf')
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))

    result_dists = dijkstra(0)
    print(f'#{tc} {result_dists[V]}')
