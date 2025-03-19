import sys
sys.stdin = open('sample_input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    ref_x = find(x)
    ref_y = find(y)
    if ref_x != ref_y:
        parent[ref_y] = ref_x

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    parent = list(range(N + 1))

    pairs = list(zip(arr[::2], arr[1::2]))
    for a, b in pairs:
        union(a, b)

    result = set()
    for i in range(1, N + 1):
        result.add(find(i))

    print(f'#{tc} {len(result)}')


# def dfs(node):
#     stack = [node]
#     while stack:
#         cur_node = stack.pop()
#         for next_node in graph[cur_node]:
#             if not visited[next_node]:
#                 visited[next_node] = True
#                 stack.append(next_node)
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     graph = [[] for _ in range(N + 1)]
#     visited = [False] * (N + 1)
#
#     for i in range(0, len(arr), 2):
#         graph[arr[i]].append(arr[i + 1])
#         graph[arr[i + 1]].append(arr[i])
#
#     cnt = 0
#     for i in range(1, N + 1):
#         if not visited[i]:
#             visited[i] = True
#             dfs(i)
#             cnt += 1
#
#     print(f'#{tc} {cnt}')






