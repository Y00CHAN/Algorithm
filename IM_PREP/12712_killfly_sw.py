T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0,0,1,-1,1,-1,1,-1]
    dj = [1,-1,0,0,-1,1,1,-1]

    max_num_1 = 0
    max_num_2 = 0

    for i in range(N):
        for j in range(N):
            lst_1 = []
            lst_1.append(arr[i][j])
            for p in range(4):
                for k in range(1, M):
                    ni = i + di[p] * k
                    nj = j + dj[p] * k
                    if 0 <= ni < N and 0 <= nj < N:
                        lst_1.append(arr[ni][nj])
            if max_num_1 < sum(lst_1):
                max_num_1 = sum(lst_1)

            lst_2 = []
            lst_2.append(arr[i][j])
            for q in range(4,8):
                for k in range(1, M):
                    ni = i + di[q] * k
                    nj = j + dj[q] * k
                    if 0 <= ni < N and 0 <= nj < N:
                        lst_2.append(arr[ni][nj])
            if max_num_2 < sum(lst_2):
                max_num_2 = sum(lst_2)

    print(f'#{tc} {max(max_num_1, max_num_2)}')

