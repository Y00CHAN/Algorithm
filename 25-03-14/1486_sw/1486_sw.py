import sys
sys.stdin = open('input (6).txt', 'r')
sys.stdout = open('output_1.txt', 'w')

def combination(lst, idx = 0, current_com=[]):

    if sum(current_com) >= B:
        result.append(current_com)
    if idx == N:
        return

    combination(lst, idx + 1, current_com)

    combination(lst, idx + 1, current_com + [lst[idx]])

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    result = []
    combination(arr)
    answer = float('inf')
    for row in result:
        if sum(row) <= answer:
            answer = sum(row)
    print(f'#{tc} {answer - B}')

