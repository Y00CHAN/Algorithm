# 21:00
T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    carry = 0

    for num in container:
        if num > max(truck):
            container.remove(num)

    while max(truck) >= max(container):
        carry += max(container)
        truck.remove(max(truck))
        container.remove((max(container)))
        if not truck or not container:
            break
        for num in container:
            if num > max(truck):
                container.remove(num)

    print(f'#{tc} {carry}')



