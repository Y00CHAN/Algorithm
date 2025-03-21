import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def dfs(i, cnt, total):
    global battery

    if total >= battery:
        return

    if cnt == N - 1:
        battery = min(battery, total + arr[i][0])
        return

    for row in range(1, N):
        if visited[row] == 0:
            visited[row] = 1
            dfs(row, cnt + 1, total + arr[i][row])
            visited[row] = 0



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    battery = float('inf')
    dfs(0, 0, 0)
    print(f'#{tc} {battery}')








