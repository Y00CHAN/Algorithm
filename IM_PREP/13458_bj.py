N = int(input())
arr = list(map(int, input().split()))
B, C = list(map(int, input().split()))

counter = 0

for i in range(N):
    arr[i] = arr[i] - B
    counter += 1

for j in range(N):
    if arr[j] > 0:
        if arr[j] % C == 0:
            counter += arr[j] // C
        else:
            counter += arr[j] // C + 1

print(counter)

