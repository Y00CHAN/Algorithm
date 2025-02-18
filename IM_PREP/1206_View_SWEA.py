for tc in range(1, 10 + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    count = 0
    for i in range(2, N - 2):
        max_surrounding = max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])
        if arr[i] > max_surrounding:
            count += arr[i] - max_surrounding

    print(f'#{tc} {count}')


