import sys
sys.stdin = open('sample_input(2).txt', 'r')
sys.stdout = open('output_1.txt', 'w')

# 1. 분할 : 리스트의 길이가 1일 때까지 분할
# 2. 정복 : 리스트의 길이가 1이 되면 자동으로 정렬됨
# 3. 병합 : 왼쪽, 오른쪽 리스트 중 작은 원소부터 정답 리스트에 추가하면서 진행

def merge(llst, rlst):
    result = [0] * (len(llst) + len(rlst))
    l = r = 0

    # 두 리스트에서 비교할 대상이 남아있을 때 까지 반복
    while l < len(llst) and r < len(rlst):
        if llst[l] < rlst[r]:
            result[l + r] = llst[l]
            l += 1
        else:
            result[l + r] = rlst[r]
            r += 1

    while l < len(llst):
        result[l + r] = llst[l]
        l += 1

    while r < len(rlst):
        result[l + r] = rlst[r]
        r += 1

    return result

def merge_sort(lst):

    global cnt

    if len(lst) == 1:
        return lst

    # 1. 분할
    mid = len(lst) // 2  # 전체 길이의 반을 인덱스로
    left = lst[:mid]
    right = lst[mid:]

    left_list = merge_sort(left)  # 쭉쭉 반 갈라가면서 들어가다가 하나 남은 시점까지 들어감
    right_list = merge_sort(right)

    if left_list[-1] > right_list[-1]:
        cnt += 1

    # print(left_list, right_list)

    # 2. 병합
    merged_list = merge(left_list, right_list)  # 머지하는 함수를 따로 만들어주자

    return merged_list

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    sorted_arr = merge_sort(arr)
    print(f'#{tc} {sorted_arr[N//2]} {cnt}')



