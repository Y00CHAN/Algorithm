from collections import deque
import sys
sys.stdin = open('sample_input (3).txt', 'r')
sys.stdout = open('output.txt', 'w')

def dfs(node):

    order = []
    if not end[node]:  # 들어온 노드가 지목받고있지 않다면
        order.append(node)
        end[start[node]].popleft()
        dfs(start[node])

    else:
        return

    return order


for tc in range(1, 11):
    V, E = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    start = [deque() * (V + 1) for _ in range(V + 1)]
    end = [deque() * (V + 1) for _ in range(V + 1)]
    worked = [deque() * (V + 1) for _ in range(V + 1)]

    for i in range(V - 1):
        s, e = arr[2 * i], arr[2 * i + 1]
        start[s].append(e)
        end[e].append(s)


    # for node in range(1, V + 1):
    #     dfs(node)
    print(end)
