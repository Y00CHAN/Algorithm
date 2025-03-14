T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    cheese_list = list(map(int, input().split()))

    pizza_queue = [0] * N
    front = rear = 0

    for i in range(N):
        pizza_queue[rear] = (cheese_list[i], i)
        rear += 1

    while True:
        cheese, idx = pizza_queue[front]
        cheese = cheese // 2
        pizza_queue[front] = cheese, idx
        if not cheese:
            if rear < M:
                cheese = cheese_list[rear]
                idx = rear
                rear += 1
            elif rear >= M:
                cheese = 0
        pizza_queue[front] = cheese, idx
        front += 1
        if front >= N:
            front = front % N

        lst = []
        for row in pizza_queue:
            if row[0] > 0:
                lst.append(row)
        if len(lst) == 1:
            print(f'#{tc} {lst[0][1] + 1}')
            break

