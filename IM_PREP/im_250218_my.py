T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    move_max = 0

    for i in range(N):
        for j in range(N):
            ci, cj = i, j
            total_moves = 0     # 왜 1일까? 문제에 출발지점부터 1 이란말이 있었나?

            for step in range(N*N):
                around_min_num = 1000
                next_i, next_j = 0, 0
                move = 0

                for k in range(4):
                    ni = ci + di[k]
                    nj = cj + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] < arr[ci][cj]:
                        if around_min_num > arr[ni][nj]:
                            around_min_num = arr[ni][nj]
                            next_i, next_j = ni, nj
                            move += 1

                if move != 0:
                    total_moves += 1
                    ci, cj = next_i, next_j
                else:
                    break

            if move_max < total_moves:
                move_max = total_moves

    print(f'#{tc} {move_max}')

