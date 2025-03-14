# # 20:26
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(str, input())) for _ in range(N)]
#
#     lst_col = list(map(list, zip(*arr))) # 전치행렬
#     print(arr)
#     print(lst_col)
#     result = 'NO'
#
#     for i in range(N):
#         for j in range(N):
#             # 가로 검사
#             if j + 5 <= N and arr[i][j] == 'o' and '.' not in arr[i][j:j + 5]:
#                 result = 'YES'
#             # 세로 검사
#             if j + 5 <= N and lst_col[i][j] == 'o' and '.' not in lst_col[i][j:j + 5]:
#                 result = 'YES'
#             # 오른쪽 위에서 왼쪽 아래로 대각선 검사
#             count = 0
#             for k in range(1, 5):
#                 ni = i + k
#                 nj = j - k
#                 if 0 <= ni < N and 0 <= nj < N and arr[i][j] == 'o' and arr[ni][nj] == 'o':
#                     count += 1
#             if count >= 4:
#                 result = 'YES'
#             # 왼쪽 위에서 오른쪽 아래로 대각선 검사
#             counter = 0
#             for h in range(1, 5):
#                 ni = i + h
#                 nj = j + h
#                 if 0 <= ni < N and 0 <= nj < N and arr[i][j] == 'o' and arr[ni][nj] == 'o':
#                     counter += 1
#             if counter >= 4:
#                 result = 'YES'
#
#     print(f'#{tc} {result}')
#

lst = [1, 2, 3, 4, 5]
a = " ".join(map(str, lst))
print(a)
