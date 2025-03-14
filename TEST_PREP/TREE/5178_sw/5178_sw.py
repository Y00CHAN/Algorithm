import sys
sys.stdin = open('5178_input.txt', 'r')
sys.stdout = open('output_1.txt', 'w')

def bst(i):

    if tree[i] != 0:
        return

    if 2 * i <= N:
        bst(i*2)

    if 2 * i + 1 <= N:
        bst(2 * i + 1)

    if 2 * i + 1 <= N:
        tree[i] = tree[2 * i] + tree[2 * i + 1]

    else:
        tree[i] = tree[2 * i]

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    tree = [0] * (N + 1)
    for i in range(M):
        tree[arr[i][0]] = arr[i][1]

    bst(1)

    print(f'#{tc} {tree[L]}')



