
T = int(input())
for tc in range(1, T+1):
    arr = list(map(str, input()))

    def is_couple(arr):

        stack = []
        for char in arr:
            if char == '(' or char == '{':
                stack.append(char)
            elif char == ')':
                if not stack or stack[-1] != '(':
                    return 0
                else:
                    stack.pop()
            elif char == '}':
                if not stack or stack[-1] != '{':
                    return 0
                else:
                    stack.pop()

        if not stack:
            return 1
        if stack:
            return 0

    result = is_couple(arr)
    print(f'#{tc} {result}')

