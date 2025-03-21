import sys
sys.stdin = open('sample_input (4).txt', 'r')
sys.stdout = open('output.txt', 'w')

def check(A, B):
    cnt = 0
    for num in A:
        if num in B:
            cnt += 1
    return cnt

T = int(input())
for tc in range(1, T + 1):
    s1, e1, s2, e2 = map(int, input().split())

    if e1 <= s2 or e2 <= s1:
        print(f'#{tc}', 0)
    else:
        lst_1 = list(range(s1, e1+1))
        lst_2 = list(range(s2, e2+1))
        if len(lst_1) > len(lst_2):
            print(f'#{tc}', check(lst_2, lst_1) - 1)
        else:
            print(f'#{tc}', check(lst_1, lst_2) - 1)







