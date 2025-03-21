import sys
sys.stdin = open('re_sample_input.txt', 'r')
sys.stdout = open('output.txt', 'w')

import heapq


def prim(tax):
    pq = [(0, 0)]
    visited = [0] * N
    min_cost = 0

    dists = [float('inf')] * N
    dists[0] = 0

    while pq:
        cost, node = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = 1
        min_cost += cost

        for next_node in range(N):
            if visited[next_node]:
                continue

            new_cost = ((x_list[next_node] - x_list[node]) ** 2 + (y_list[next_node] - y_list[node]) ** 2) * tax

            if new_cost < dists[next_node]:
                dists[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    return round(min_cost)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())

    result = prim(tax)
    print(f'#{tc} {result}')



