T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    visited = [[0] * N for _ in range(N)]  # 방문 기록

    q = []  # q에 옮겨진 좌표들을 인큐, 디큐 할 예정
    si, sj = 0, 0
    min_visit = []
    result = 0

    for i in range(N):  # 시작 좌표 찾기
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j

    q.append((si, sj))  # 시작점부터 쭉 탐색
    visited[si][sj] = 1

    while q:
        ci, cj = q[0]  # 현재 위치는 q의 0번째 요소.

        if not q:  # q가 비게되면 미로를 못푸는 것
            print(f'#{tc} {-1}')
            break

        for p in range(4):  # 탐색 후 새로운 좌표를 q에 인큐하고 있던 좌표는 디큐해준다
            ni = ci + di[p]
            nj = cj + dj[p]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if arr[ni][nj] == 3:  # 도착점을 만나면 결과값 변경
                    min_visit.append(visited[ci][cj] + 1)
                if arr[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[ci][cj] + 1
                if arr[ni][nj] == 4:  # 점프대를 만나면 2칸 탐색 후 0이 있으면 이동
                    visited[ni][nj] = visited[ci][cj] + 1
                    for k in range(4):
                        ki = ni + di[k] * 2
                        kj = nj + dj[k] * 2
                        if 0 <= ki < N and 0 <= kj < N and not visited[ki][kj] and not arr[ki][kj]:
                            q.append((ki, kj))
                            visited[ki][kj] = visited[ni][nj] + 1

        q.pop(0)

    print(f'#{tc} {min(min_visit)}')







