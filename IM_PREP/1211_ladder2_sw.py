from collections import deque

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    di = [0, 0, 1]
    dj = [1, -1, 0]

    start_list = []

    for j in range(100):
        if arr[0][j] == 1:
            start_list.append((0, j))

    min_num = 100000
    max_idx = 0

    for i, j in start_list:
        ci, cj = i, j
        visited = [[0] * 100 for _ in range(100)]

        while start_list:

            for p in range(3):
                ni = ci + di[p]
                nj = cj + dj[p]
                if 0 <= ni < 100 and 0 <= nj < 100 and not visited[ni][nj] and arr[ni][nj]:
                    visited[ni][nj] = visited[ci][cj] + 1
                    ci, cj = ni, nj

            if ci == 99:
                if visited[ci][cj] < min_num:
                    min_num = visited[ci][cj]
                    max_idx = j
                    break

    print(f'#{T} {max_idx}')



