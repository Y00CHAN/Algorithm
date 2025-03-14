friends = ['A', 'B', 'C', 'D', 'E']
n = len(friends)

def get_sub(tar):
    sub_list = []
    for i in range(n):
        # 각각 원소가 포함되어 있나요?
        if tar & 0x1:  # 1이라고 해도 되지만 비트연산임을 명시하기위해 0x1 사용.
            sub_list.append(friends[i])
        tar >>= 1  # 맨 우측 비트를 삭제한다. 즉, 다음 원소를 확인하겠다.
    return sub_list

result = 0
for target in range(1<<n):
    print(get_sub(target))
    if len(get_sub(target)) >= 2:
        result += 1

print(f'두명 이상이 가는 경우의 수 : {result}')
