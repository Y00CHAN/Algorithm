# 19:45
T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    splash = [[0] * M for _ in range(M)]
    max_kill = 0
    for i in range(N):
        for j in range(N):
            killfly = 0
            for p in range(M):
                for q in range(M):
                    if 0 <= p + i < N and 0 <= q + j < N:
                        killfly += arr[p + i][q + j]
            if max_kill < killfly:
                max_kill = killfly

    print(f'#{tc} {max_kill}')