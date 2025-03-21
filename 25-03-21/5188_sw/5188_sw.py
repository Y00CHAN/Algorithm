import sys
sys.stdin = open('5188_input.txt', 'r')
sys.stdout = open('output.txt', 'w')

from collections import deque

di = [0,0,1,-1]
dj = [1,-1,0,0]

def dfs(i, j, sum_num):
    global result
    q = deque([[i, j, sum_num]])

    while q:
        p = q.popleft()
        visited[p[0]][p[1]] = 1

        if p in q:
            continue

        if p[2] >= result:
            continue

        if p[0] == N - 1 and p[1] == N - 1:
            result = min(p[2], result)

        for k in range(4):
            ni = p[0] + di[k]
            nj = p[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                q.append([ni, nj, p[2] + arr[ni][nj]])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * (N + 1) for _ in range(N + 1)]
    result = float('inf')
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {result}')
