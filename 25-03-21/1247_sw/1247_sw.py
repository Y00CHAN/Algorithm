import sys
sys.stdin = open('input (3).txt', 'r')
sys.stdout = open('output.txt', 'w')

from collections import deque

def dfs(spot):
    pass


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    office = (arr[0], arr[1])
    home = (arr[2], arr[3])

    dfs(home)












