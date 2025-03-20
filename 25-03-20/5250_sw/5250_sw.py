import sys
sys.stdin = open('5250_input.txt', 'r')
sys.stdout = open('output.txt', 'w')

import heapq

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [[INF] * N for _ in range(N)]
    dists[start_node[0]][start_node[1]] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if dists[node[0]][node[1]] < dist:
            continue

        for k in range(4):
            ni = node[0] + di[k]
            nj = node[1] + dj[k]

            if 0 <= ni < N and 0 <= nj < N:
                next_dist = arr[ni][nj] - arr[node[0]][node[1]]
                if next_dist <= 0:
                    next_dist = 0
                next_node = (ni, nj)

                new_dist = dist + next_dist + 1

                if dists[next_node[0]][next_node[1]] <= new_dist:
                    continue

                dists[next_node[0]][next_node[1]] = new_dist

                heapq.heappush(pq, (new_dist, next_node))

    return dists


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    INF = float('inf')

    result_dists = dijkstra((0, 0))
    print(f'#{tc} {result_dists[N-1][N-1]}')

