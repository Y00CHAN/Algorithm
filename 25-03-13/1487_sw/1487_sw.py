import sys
sys.stdin = open('sample_input (4).txt', 'r')
sys.stdout = open('output.txt', 'w')

def run(tar):
    global cnt
    sub_list = []
    for i in range(N):
        if tar & 0x1:
            sub_list.append(arr[i])
        tar >>= 1
    return sub_list

T = int(input())
for tc in range(1, T + 1):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    for target in range(1<<N):
        lst = run(target)
        if sum(lst) == S:
            cnt += 1

    print(cnt)

    '''
    구현은 완료됐고 8번 tc까지는 통과 
    그 이후로는 런타임 에러 뜨는듯.. 다음에 잡아보자
    그리고 SWEA에 파이썬 제출 없어서 제출 못함
    '''