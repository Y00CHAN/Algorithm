T = int(input())
for tc in range(1, 1 + T):
    N, M = list(map(int, input().split()))
    first_stage = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(M)]

    a, b, c = 0, 0, 0

    for row in arr:  # row 의 수가 결국 반복 횟수
        [a, b, c] = row
        for k in range(1, c + 1):
            if b - 1 + k > N - 1 or b - 1 - k < 0:  # 범위에서 벗어날경우 멈춘다
                break
            if first_stage[b - 1 + k] == first_stage[b - 1 - k]:  # 기준으로부터 k만큼 거리에 있는 두 깃발 상태가 같으면 변경
                if first_stage[b - 1 + k] == 1:
                    first_stage[b - 1 + k] = 0
                else:
                    first_stage[b - 1 + k] = 1
                if first_stage[b - 1 - k] == 1:
                    first_stage[b - 1 - k] = 0
                else:
                    first_stage[b - 1 - k] = 1

    print(f'#{tc}', *first_stage)
