from collections import deque


for tc in range(1, 10 + 1):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    di = [0, 0, 1]  # 우, 좌, 하
    dj = [1, -1, 0]

    start_list = [(0, j) for j in range(100) if arr[0][j] == 1]  # 시작점 목록

    min_num = float('inf')
    max_idx = 0

    for i, j in start_list:
        ci, cj = i, j
        visited = [[0] * 100 for _ in range(100)]  # 방문 체크
        visited[ci][cj] = 1  # 시작점 방문 처리
        dist = 0  # 이동 거리

        while True:
            moved = False  # 이동 여부 체크

            for p in range(3):  # 우 → 좌 → 하 순서 탐색
                ni = ci + di[p]
                nj = cj + dj[p]

                if 0 <= ni < 100 and 0 <= nj < 100 and not visited[ni][nj] and arr[ni][nj]:
                    visited[ni][nj] = 1
                    ci, cj = ni, nj
                    dist += 1
                    moved = True
                    break  # 한 방향으로 이동했으면 다른 방향 탐색 안 함

            if not moved:  # 더 이상 이동할 수 없으면 종료
                break

        if ci == 99 and dist < min_num:
            min_num = dist
            max_idx = j  # 시작점의 j값 저장

    print(f'#{T} {max_idx}')