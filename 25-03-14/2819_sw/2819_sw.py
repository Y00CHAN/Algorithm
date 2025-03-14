import sys
sys.stdin = open('sample_input (5).txt', 'r')
sys.stdout = open('output_1.txt', 'w')

di = [0,0,1,-1]
dj = [1,-1,0,0]

def dfs(i, j, num):
    if len(num) == 7:
        result.add(num)
        return

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if ni < 0 or ni >= 4 or nj < 0 or nj >= 4:
            continue

        dfs(ni, nj, num + arr[ni][nj])

T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(str, input().split())) for _ in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])

    print(f'#{tc} {len(result)}')
