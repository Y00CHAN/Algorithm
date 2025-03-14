import sys
sys.stdin = open('5176_input.txt', 'r')
sys.stdout = open('output_1.txt', 'w')

def bst(i):
    global num
    if i <= N:
        bst(i * 2)
        tree[i] = num
        num += 1
        bst(i * 2 + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    num = 1
    bst(1)

    print(tree)

