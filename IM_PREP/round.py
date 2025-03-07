T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    direction = 0
    i, j = 0, 0
    num = 1

    while num <= N ** 2:

        arr[i][j] = num
        num += 1

        ni = i + di[direction]
        nj = j + dj[direction]

        if not (0 <= ni < N and 0 <= nj < N) or arr[ni][nj] != 0:
            direction = (direction + 1) % 4
            ni = i + di[direction]
            nj = j + dj[direction]

        i, j = ni, nj

    print(f'#{tc}')
    for row in arr:
        print(*row)
