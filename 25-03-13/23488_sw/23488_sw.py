import sys
sys.stdin = open('sample_input(3).txt', 'r')
sys.stdout = open('output.txt', 'w')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    weight.sort()
    truck.sort()

    cnt = 0
    while True:

        if weight[-1] > truck[-1]:
            weight.pop()
        else:
            truck.pop()
            cnt += weight.pop()

        if not truck or not weight:
            break

    print(f'#{tc} {cnt}')




