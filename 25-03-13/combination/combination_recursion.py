arr = ['A', 'B', 'C', 'D', 'E']
path = []

n = 3
def run(cnt, start):
    if cnt == n:
        print(*path)
        return

    for i in range(start, len(arr)):
        path.append(arr[i])
        run(cnt + 1, i + 1)
        path.pop()

run(0, 0)