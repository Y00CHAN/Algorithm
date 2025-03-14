def solution(numbers, hand):

    answer = []
    left = [1, 4, 7]
    right = [3, 6, 9]
    center = [2, 5, 8, 0]
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]  # 그림과 동일하게 키패드 배열

    lx, ly = 3, 0  # 초기 왼손 좌표
    rx, ry = 3, 2  # 초기 오른손 좌표
    cx, cy = -1, -1  # 초기 목표 좌표

    for num in numbers:
        for i in range(4):
            for j in range(3):
                if num == arr[i][j]:  # 입력받은 숫자가 키패드의 숫자와 같으면
                    cx, cy = i, j  # 목표 좌표가 지정됨
                    if num in left:  # 숫자가 왼쪽에 있으면 단순히 왼손 사용
                        answer.append('L')
                        lx, ly = i, j  # 항상 손가락이 움직이면 좌표를 움직여줘야한다. 다음 목표 좌표와 거리계산을 해야하기 때문
                        break
                    if num in right:  # 숫자가 오른쪽에 있으면 단순히 오른손 사용
                        answer.append('R')
                        rx, ry = i, j
                        break
                    if num in center:
                        if abs(cx - lx) + abs(cy - ly) < abs(cx - rx) + abs(cy - ry):  # 거리가 왼손이 가까울때
                            answer.append('L')
                            lx, ly = i, j
                            break
                        if abs(cx - lx) + abs(cy - ly) > abs(cx - rx) + abs(cy - ry):  # 거리가 오른손이 가까울때
                            answer.append('R')
                            rx, ry = i, j
                            break
                        if abs(cx - lx) + abs(cy - ly) == abs(cx - rx) + abs(cy - ry):  # 거리가 같을때 왼손잡이 오른손잡이 판단
                            if hand == 'left':
                                answer.append('L')
                                lx, ly = i, j
                                break
                            if hand == 'right':
                                answer.append('R')
                                rx, ry = i, j
                                break

    answer = "".join(answer)

    return answer
