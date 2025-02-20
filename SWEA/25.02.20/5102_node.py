from collections import deque

def bfs(s, e):
    visited = [0] * (V + 1)
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        t = q.popleft()
        if t == e:  # 목적지 도착하면 거리 반환
            return visited[t] - 1
        for w in adj_list[t]:
            if visited[w] == 0:
                visited[w] = visited[t] + 1
                q.append(w)

    return 0

T = int(input())
for tc in range(1, T + 1):
    V, E = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(E)]
    s, e = list(map(int, input().split()))
    adj_list = [[] for _ in range(V+1)]

    for u, v in arr:
        adj_list[u].append(v)
        adj_list[v].append(u)

    ans = bfs(s, e)
    print(f'#{tc} {ans}')

