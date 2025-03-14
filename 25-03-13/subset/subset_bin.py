arr = ['A', 'B', 'C']
n = len(arr)

def get_sub(tar):
    for i in range(n):
        # 각각 원소가 포함되어 있나요?
        if tar & 0x1:  # 1이라고 해도 되지만 비트연산임을 명시하기위해 0x1 사용.
            print(arr[i], end='')
        tar >>= 1  # 맨 우측 비트를 삭제한다. 즉, 다음 원소를 확인하겠다.

# 전체 부분집합을 확인해야한다.
for target in range(1<<n):
    print('{', end='')
    get_sub(target)
    print('}')
