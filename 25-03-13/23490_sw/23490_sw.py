import sys
sys.stdin = open('sample_input(4).txt', 'r')
sys.stdout = open('output.txt', 'w')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]

    arr.sort(key = lambda x:(x[1]))

    selected = [arr[0]]
    current_end = arr[0][1]

    for i in range(1, N):
        start, end = arr[i]
        if start >= current_end:
            selected.append(arr[i])
            current_end = end

    print(f'#{tc} {len(selected)}')




