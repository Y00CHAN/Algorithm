import sys
sys.stdin = open('5209_input (1).txt', 'r')
sys.stdout = open('output.txt', 'w')


def dfs(i, total):
    global price

    if total >= price:
        return

    if i == N:
        price = min(price, total)
        return

    for row in range(N):
        if visited[row] == 0:
            visited[row] = 1
            dfs(i + 1, total + arr[row][i])
            visited[row] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    price = float('inf')
    dfs(0, 0)
    print(f'#{tc} {price}')





