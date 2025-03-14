# from collections import deque
# import sys
# sys.stdin = open('tree_input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
#
# def dfs(tree, node):
#
#     print(node, end=' ')
#
#     if node not in tree:
#         return
#
#     for num in tree[node]:
#         dfs(tree, num)
#
# N = int(input())
# arr = list(map(int, input().split()))
#
# tree = {
#     1: [2, 3],
#     2: [4],
#     3: [5, 6],
#     4: [7],
#     5: [8, 9],
#     6: [10, 11],
#     7: [12],
#     11: [13]
# }
#
# dfs(tree, 1)
#

def preorder_traverse(T):
    if T:
        print(T, end=' ')
        if left[T] != 0:
            preorder_traverse(left[T])
        if right[T] != 0:
            preorder_traverse(right[T])


V = int(input())
arr = list(map(int, input().split()))

left = [0] * (V + 1)
right = [0] * (V + 1)

for i in range(V - 1):
    p, c = arr[2 * i], arr[2 * i + 1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

preorder_traverse(arr[0])