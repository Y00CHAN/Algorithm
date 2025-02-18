# T = int(input())
# for test_case in range(1, T + 1):
#     arr = list(map(str, input()))
#
#     def is_couple(arr):
#         stack = []
#         for char in arr:
#             if char == '(':     # 여는 괄호라면
#                 stack.append(char)  # 스택의 맨뒤에 추가
#             elif char == ')':   # 닫는 괄호라면
#                 if not stack:   # 처음에 닫는괄호로 시작한다면 False
#                     return -1
#                 else:
#                     stack.pop()     # 스택의 맨뒤를 제거(어차피 맨뒤는 여는괄호일것이다)
#         if not stack:   # 루프 다 돌렸을때 스택이 비어있으면 모두 짝이 맞음 True
#             return 1
#         else:   # 다 돌렸는데도 스택에 괄호가 남아있다면 False
#             return -1
#
#     result = is_couple(arr)
#     print(f'#{test_case} {result}')

T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    size = len(arr)
    stack = [0] * size

    top = -1
    result = 1

    for char in arr:
        if char == '(':
            top += 1
            stack[top] = char
        elif char == ')':
            if top == -1:
                result = -1
                break
            else:
                top -= 1

    if top != -1:
        result = -1

    print(f'#{tc} {result}')






