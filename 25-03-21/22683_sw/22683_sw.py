import sys
sys.stdin = open('sample_input (3).txt', 'r')
sys.stdout = open('output.txt', 'w')

di = [0,0,1,-1]
dj = [1,-1,0,0]

def get_point(arr):

    start = (0, 0)
    end = (0, 0)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                start = i, j
            if arr[i][j] == 'Y':
                end = i, j

    return start, end

def bfs():

    pass

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(str, input().strip())) for _ in range(N)]

    start, end = get_point(arr)





