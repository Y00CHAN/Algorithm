# 09:02 start
T = int(input())
for tc in range(1, T + 1):

    K, N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    print(arr)
    result = 0

    bus_stop = [0] * (N+1)

    for num in arr:
        bus_stop[num] += num

    print(bus_stop)

    start_idx = 0
    lst = []
    for i in range(start_idx, start_idx + K + 1):
        if start_idx + K + 1 <= N:
            lst.append(bus_stop[i])
            start_idx = max(lst)
            result += 1

    if arr[0] > K:
        result = 0

    for j in range(M-1):
        if arr[j+1] - arr[j] > K:
            result = 0

    print(result)
