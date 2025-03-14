T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().strip()))

    # 금액 저장하는 리스트
    change_list = [0] * 8

    N = len(arr)

    if N == 2:
        change_list[7] = arr[0]
        if arr[0] >= 5:
            change_list[7] -= 5
            change_list[6] += 1
    if N == 3:
        change_list[5] = arr[0]
        if arr[0] >= 5:
            change_list[5] -= 5
            change_list[4] += 1
        change_list[7] = arr[1]
        if change_list[7] >= 5:
            change_list[7] -= 5
            change_list[6] += 1
    if N == 4:
        change_list[3] = arr[0]
        if arr[0] >= 5:
            change_list[3] -= 5
            change_list[2] += 1
        change_list[5] = arr[1]
        if arr[1] >= 5:
            change_list[5] -= 5
            change_list[4] += 1
        change_list[7] = arr[2]
        if arr[2] >= 5:
            change_list[7] -= 5
            change_list[6] += 1
    if N == 5:
        change_list[1] = arr[0]
        if arr[0] >= 5:
            change_list[1] -= 5
            change_list[0] += 1
        change_list[3] = arr[1]
        if arr[1] >= 5:
            change_list[3] -= 5
            change_list[2] += 1
        change_list[5] = arr[2]
        if arr[2] >= 5:
            change_list[5] -= 5
            change_list[4] += 1
        change_list[7] = arr[3]
        if arr[3] >= 5:
            change_list[7] -= 5
            change_list[6] += 1
    if N == 6:
        change_list[0] = (arr[0] * 10 + arr[1]) // 5
        change_list[1] = (arr[0] * 10 + arr[1]) % 5
        change_list[3] = arr[2]
        if arr[2] >= 5:
            change_list[3] -= 5
            change_list[2] += 1
        change_list[5] = arr[3]
        if arr[3] >= 5:
            change_list[5] -= 5
            change_list[4] += 1
        change_list[7] = arr[4]
        if arr[4] >= 5:
            change_list[7] -= 5
            change_list[6] += 1
    if N == 7:
        change_list[0] = 20

    print(f'#{test_case}')
    print(*change_list)


