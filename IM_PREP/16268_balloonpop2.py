# 19:06
T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    di  = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    flower = 0
    for i in range(N):
        for j in range(M):
            center = arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    center += arr[ni][nj]
            if flower < center:
                flower = center
    print(f'#{tc} {flower}')
# 19:19