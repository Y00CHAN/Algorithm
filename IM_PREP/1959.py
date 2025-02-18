# 20:15
T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr_N = list(map(int, input().split()))
    arr_M = list(map(int, input().split()))

    if N > M:
        arr_N, arr_M = arr_M, arr_N
        N, M = M, N  # N이 항상 작은 크기

    lst = []
    for i in range(len(arr_M)):
        count = 0
        for j in range(len(arr_N)):
            if j + i < len(arr_M):
                count += (arr_M[j + i]) * (arr_N[j])
        lst.append(count)

    print(max(lst))

