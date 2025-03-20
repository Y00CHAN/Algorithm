import sys
sys.stdin = open('graph.txt', 'r')
sys.stdout = open('output.txt', 'w')


def find(x):
    if x == parents[x]:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    ref_x = find(x)
    ref_y = find(y)

    if ref_x == ref_y:
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


V, E = map(int, input().split())
graph = [[0] * V for _ in range(V + 1)]
edges = []

for _ in range(E):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

edges.sort(key=lambda x: x[2])
parents = list(range(V))

cnt = 0
result = 0

for u, v, w in edges:
    if find(u) != find(v):
        union(u, v)
        cnt += 1
        result += w

        if cnt == V - 1:
            break

print(result)
