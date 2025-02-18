
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    lst = []
    for sub in arr:
        if sub not in lst:
            lst.append(sub)

    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            if lst[j][1] > lst[j+1][1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    count = 0
    end_time = 0

    for k in range(len(lst)):
        a = lst[k][0]
        b = lst[k][1]
        if a >= end_time:
            count += 1
            end_time = b

    print(f'#{tc} {count}')

