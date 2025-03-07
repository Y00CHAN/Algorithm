T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_num = 0

    if len(A) < len(B):
        for i in range(len(B)):
            lst_1 = []
            for j in range(len(A)):
                if i + j < len(B):
                    lst_1.append(A[j] * B[i + j])
            if i <= M - N and max_num < sum(lst_1):
                max_num = sum(lst_1)

    else:
        for i in range(len(A)):
            lst_2 = []
            for j in range(len(B)):
                if i + j < len(A):
                    lst_2.append(B[j] * A[i + j])
            if i <= N - M and max_num < sum(lst_2):
                max_num = sum(lst_2)

    print(f'#{tc} {max_num}')
