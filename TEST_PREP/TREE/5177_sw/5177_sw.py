
import sys
sys.stdin = open('5177_input.txt', 'r')
sys.stdout = open('output_1.txt', 'w')

def heap(i):
    if i <= N:
        heap(i*2)
        tree[i] = min(arr)
        heap(i*2+1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    tree = [0] * (N + 1)

    heap(1)




