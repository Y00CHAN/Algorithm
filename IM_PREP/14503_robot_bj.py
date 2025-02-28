N, M = list(map(int, input().split()))         # 3: 40 start
r, c, d = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]

di = [-1, 0, 1, 0]  # 상 우 하 좌
dj = [0, 1, 0, -1]

visited = [[0] * M for _ in range(N)]

x, y = r, c  # 현재 로봇청소기의 위치

while True:

    arr[x][y] = 2  # 현재 위치 청소

    surround = []

    for q in range(4):
        ni = x + di[q]
        nj = y + dj[q]
        surround.append(arr[ni][nj])

    if 0 in surround:  # 만약 상하좌우에 청소안한칸이 있으면
        if d == 0:
            d = 3
            ci = x + di[d]
            cj = y + dj[d]
            if 0 <= ci < N and 0 <= cj < M and arr[ci][cj] == 0:
                arr[ci][cj] = 2
                x, y = ci, cj
                continue

        if d == 1:
            d = 0
            ci = x + di[d]
            cj = y + dj[d]
            if 0 <= ci < N and 0 <= cj < M and arr[ci][cj] == 0:
                arr[ci][cj] = 2
                x, y = ci, cj
                continue

        if d == 2:
            d = 1
            ci = x + di[d]
            cj = y + dj[d]
            if 0 <= ci < N and 0 <= cj < M and arr[ci][cj] == 0:
                arr[ci][cj] = 2
                x, y = ci, cj
                continue

        if d == 3:
            d = 2
            ci = x + di[d]
            cj = y + dj[d]
            if 0 <= ci < N and 0 <= cj < M and arr[ci][cj] == 0:
                arr[ci][cj] = 2
                x, y = ci, cj
                continue

    if 0 not in surround:  # 만약 상하좌우에 청소 안한곳이 없으면
        if d == 0:
            ci = x + di[2]  # 뒤로 한칸 좌표
            cj = y + dj[2]
            if 0 <= ci < N and 0 <= cj < M and arr[ci][cj] == 1:
                break
            else:
                x, y = ci, cj

        if d == 1:
            ci = x + di[3]  # 뒤로 한칸 좌표
            cj = y + dj[3]
            if 0 <= ci < N and 0 <= cj < M and arr[ci][cj] == 1:
                break
            else:
                x, y = ci, cj

        if d == 2:
            ci = x + di[0]  # 뒤로 한칸 좌표
            cj = y + dj[0]
            if 0 <= ci < N and 0 <= cj < M and arr[ci][cj] == 1:
                break
            else:
                x, y = ci, cj

        if d == 3:
            ci = x + di[1]  # 뒤로 한칸 좌표
            cj = y + dj[1]
            if 0 <= ci < N and 0 <= cj < M and arr[ci][cj] == 1:
                break
            else:
                x, y = ci, cj



lst = []
for row in arr:
    for num in row:
        lst.append(num)

print(lst.count(2))

