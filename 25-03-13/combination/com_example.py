arr = [1,2,3,4,5,6]
path = []

n = 3
def run(cnt, start):
    if cnt == n:
        print(path)
        return

    for i in range(start, len(arr)):
        path.append(arr[i])
        run(cnt + 1, i)
        path.pop()

run(0, 0)


