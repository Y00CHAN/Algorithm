from collections import deque

def bfs(i, j):
    visited = [[0] * 16 for _ in range(16)]
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    while q:
        ti, tj = q.popleft()
        for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
            wi, wj = ti + di, tj + dj
            if 0 <= wi < 100 and 0 <= wj < 16 and not visited[wi][wj] and arr[wi][wj] != 1:
                visited[wi][wj] = 1
                q.append([wi, wj])
                if arr[wi][wj] == 3:
                    return 1
    return 0

def find_start(n):
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                return i, j

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(16)]


    sti, stj = find_start(16)

    ans = bfs(sti, stj)

    print(f'#{tc} {ans}')
