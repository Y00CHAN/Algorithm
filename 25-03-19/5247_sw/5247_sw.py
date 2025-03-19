import sys
sys.stdin = open('5247_input.txt', 'r')
sys.stdout = open('output.txt', 'w')

from collections import deque

def cal(num):
    q = deque([(num, 0)])
    visited[num] = 1

    while q:
        p, depth = q.popleft()

        if p == M:
            print(f'#{tc} {depth}')
            return

        if p <= 0:
            continue

        next_lst = [p + 1, p - 1, p * 2, p - 10]

        for next_p in next_lst:
            if 0 <= next_p <= max_size and not visited[next_p]:
                visited[next_p] = 1
                q.append((next_p, depth + 1))

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    max_size = max(N, M) * 2
    visited = [0] * (max_size + 1)

    cal(N)

