import sys
sys.stdin = open('5207_input.txt', 'r')
sys.stdout = open('output_1.txt', 'w')

def binary_search_recur(left, right, target, dir = ''):
    # left, right 를 작업 영역으로 검색
    # left <= right 만족하면 반복..
    global result

    if left > right:
        return

    mid = (left + right) // 2
    # 검색하면 종료
    if target == A[mid]:
        result += 1
        return

    # 한 번 할 때마다 left 와 right 를 mid 기준으로 이동시켜 주면서 진행
    # 왼쪽을 봐야한다.
    if target < A[mid]:
        dir = 'l'
        return binary_search_recur(left, mid - 1, target, dir)
    # 오른쪽을 봐야한다.
    else:
        dir = 'r'
        return binary_search_recur(mid + 1, right, target, dir)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    result = 0
    for num in B:
        binary_search_recur(0, len(A) - 1, num)
    print(f'#{tc} {result}')





