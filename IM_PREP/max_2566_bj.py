arr = [list(map(int, input().split())) for _ in range(9)]

ci, cj = 0, 0
num_max = 0

for i in range(9):
    for j in range(9):
        if num_max < arr[i][j]:
            num_max = arr[i][j]
            ci, cj = i, j

print(num_max)
print(ci+1, cj+1)
