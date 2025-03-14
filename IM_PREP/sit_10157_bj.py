N, M = list(map(int, input().split()))
K = int(input())
arr = [[0] * M for _ in range(N)]

if K > N*M:
    print(0)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

i, j = 0, 0
num = 1
direction = 0

while num <= N * M:
    if num == K:
        print(i+1, j+1)
        break
    arr[i][j] = num
    num += 1

    ni = i + di[direction]
    nj = j + dj[direction]

    if not (0 <= ni < N and 0 <= nj < M) or arr[ni][nj] != 0:
        direction = (direction + 1) % 4
        ni = i + di[direction]
        nj = j + dj[direction]

    i, j = ni, nj







