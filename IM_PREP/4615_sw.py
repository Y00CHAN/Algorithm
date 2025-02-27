# T = int(input())
# for tc in range(1, T + 1):
#     N, M = list(map(int, input().split()))
#     arr = [list(map(int, input().split())) for _ in range(M)]
#
#     visited = [[0] * N for _ in range(N)]
#
#     if N == 4:
#         visited[1][1] = 2
#         visited[1][2] = 1
#         visited[2][1] = 1
#         visited[2][2] = 2
#
#     if N == 6:
#         visited[2][2] = 2
#         visited[3][2] = 1
#         visited[2][3] = 1
#         visited[3][3] = 2
#
#     if N == 8:
#         visited[3][3] = 2
#         visited[4][3] = 1
#         visited[3][4] = 1
#         visited[4][4] = 2
#
#     di = [0, 0, -1, 1, 1, 1, -1, -1]
#     dj = [1, -1, 0, 0, -1, 1, 1, -1]
#
#     x, y = 0, 0  # 돌 놓는 위치
#
#     for k in range(M):
#         x = arr[k][1] - 1  # 좌표와 배열과 다른것 바꿔주기
#         y = arr[k][0] - 1
#         visited[x][y] = arr[k][2]
#         for p in range(8):
#             for q in range(1, N):
#                 ni = x + di[p] * q
#                 nj = y + dj[p] * q
#                 if 0 <= ni < N and 0 <= nj < N:
#                     if visited[ni][nj] == 0:
#                         break
#                     if visited[x][y] == 1 and visited[ni][nj] == 1:
#                         for b in range(1, q):
#                             bi = x + di[p] * b
#                             bj = y + dj[p] * b
#                             if visited[bi][bj] == 0:
#                                 break
#                             else:
#                                 visited[bi][bj] = 1
#                     if visited[x][y] == 2 and visited[ni][nj] == 2:
#                         for b in range(1, q):
#                             bi = x + di[p] * b
#                             bj = y + dj[p] * b
#                             if visited[bi][bj] == 0:
#                                 break
#                             else:
#                                 visited[bi][bj] = 2
#
#     lst = []
#     for row in visited:
#         for num in row:
#            lst.append(num)
#
#     print(f'#{tc} {lst.count(1)} {lst.count(2)}')


T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(M)]

    visited = [[0] * N for _ in range(N)]

    if N == 4:
        visited[1][1] = 2
        visited[1][2] = 1
        visited[2][1] = 1
        visited[2][2] = 2

    if N == 6:
        visited[2][2] = 2
        visited[3][2] = 1
        visited[2][3] = 1
        visited[3][3] = 2

    if N == 8:
        visited[3][3] = 2
        visited[4][3] = 1
        visited[3][4] = 1
        visited[4][4] = 2

    di = [0, 0, -1, 1, 1, 1, -1, -1]
    dj = [1, -1, 0, 0, -1, 1, 1, -1]

    x, y = 0, 0  # 돌 놓는 위치

    for k in range(M):
        if k >= len(arr):  # 인덱스 초과 방지
            break

        x = arr[k][1] - 1  # 좌표와 배열과 다른 것 보정
        y = arr[k][0] - 1

        if visited[x][y] != 0:  # 이미 돌이 놓인 곳이면 무시
            continue

        visited[x][y] = arr[k][2]

        for p in range(8):
            for q in range(1, N):
                ni = x + di[p] * q
                nj = y + dj[p] * q

                if not (0 <= ni < N and 0 <= nj < N):  # 범위 밖이면 중단
                    break

                if visited[ni][nj] == 0:  # 빈 공간을 만나면 중단
                    break

                if visited[ni][nj] == visited[x][y]:  # 같은 색 돌을 만나면 뒤집기
                    for b in range(1, q):
                        bi = x + di[p] * b
                        bj = y + dj[p] * b
                        visited[bi][bj] = visited[x][y]
                    break

    lst = []
    for row in visited:
        for num in row:
            lst.append(num)

    print(f'#{tc} {lst.count(1)} {lst.count(2)}')




