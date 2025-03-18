import sys
sys.stdin = open('5208_input.txt', 'r')
sys.stdout = open('output_1.txt', 'w')

def dfs(cur, move, cnt):
    global min_cnt

    if cur >= arr[0] - 1:
        min_cnt = min(min_cnt, cnt)
        return

    for i in range(1, move + 1):
        if cur + i < arr[0] and cnt + 1 < min_cnt:
            dfs(cur + i, arr[cur + i], cnt + 1)

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    min_cnt = float('inf')

    dfs(1,arr[1],0)
    print(f'#{tc} {min_cnt - 1}')























