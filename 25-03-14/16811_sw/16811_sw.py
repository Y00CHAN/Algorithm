from collections import deque
import sys
sys.stdin = open('sample_in.txt', 'r')
sys.stdout = open('output_1.txt', 'w')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort()




