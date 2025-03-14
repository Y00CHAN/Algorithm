import sys
sys.stdin = open('input (5).txt', 'r')
sys.stdout = open('output_1.txt', 'w')

di = [-1,1,0,0]
dj = [0,0,1,-1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * (N * N + 1)

    for i in range(N):
        for j in range(N):
            for p in range(4):
                ni = i + di[p]
                nj = j + dj[p]
                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    continue

                if arr[i][j] + 1 == arr[ni][nj]:
                    visited[arr[i][j]] = 1
                    break

    max_cnt = cnt = start = 0
    for i in range(1, N * N + 1):
        if visited[i] == 1:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
                start = i - cnt
            cnt = 0

    print(f'#{tc} {start} {max_cnt + 1}')












