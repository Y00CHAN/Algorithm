T = int(input())
for tc in range(1, 1+T):
    arr = list(map(str, input()))

    stack = []       #len(stack)이 답
    for i in range(len(arr)-1):
        stack.append(arr[i])
        if arr[i+1] == stack[-1]:
            stack.pop()

    print(stack)




    # print(arr)
        # for j in range(i+1, len(arr)):
        #     if arr[j] == arr[i]:
        #         stack.pop(i)


