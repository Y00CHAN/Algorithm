T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]  # 상, 하, 좌, 우 방향 정의
    dj = [0, 0, -1, 1]

    max_moves = 0  # 최대 이동 횟수 저장

    for i in range(N):
        for j in range(N):
            moves = 1  # 현재 위치에서 시작하는 이동 횟수
            ci, cj = i, j  # 현재 위치

            while True:  # 더 이상 이동할 곳이 없을 때까지 반복
                around_min_num = float('inf')
                next_i, next_j = -1, -1
                move_possible = False

                for k in range(4):  # 상하좌우 탐색
                    ni = ci + di[k]
                    nj = cj + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and arr[ci][cj] > arr[ni][nj]:
                        if arr[ni][nj] < around_min_num:  # 가장 작은 숫자가 있는 방향 찾기
                            around_min_num = arr[ni][nj]
                            next_i, next_j = ni, nj
                            move_possible = True

                if move_possible:
                    moves += 1
                    ci, cj = next_i, next_j  # 다음 위치로 이동
                else:
                    break  # 더 이상 이동할 곳이 없으면 종료

            max_moves = max(max_moves, moves)  # 최댓값 갱신

    print(f"#{tc} {max_moves}")
