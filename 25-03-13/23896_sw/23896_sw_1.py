import sys
sys.stdin = open('5203_input.txt', 'r')
sys.stdout = open('output_1.txt', 'w')

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    player_1 = []
    player_2 = []
    result = 0

    for i in range(12):
        if i % 2 == 0:
            player_1.append(arr[i])
            player_1_sorted = sorted(player_1)
            player_1_set = list(set(player_1_sorted))
            for j in range(len(player_1_sorted) - 2):
                if player_1_sorted[j] == player_1_sorted[j + 1] == player_1_sorted[j + 2]:
                    result = 1
                    break
            for j in range(len(player_1_set) - 2):
                if player_1_set[j] + 1 == player_1_set[j + 1] and player_1_set[j + 1] + 1 == player_1_set[j + 2]:
                    result = 1
                    break

            if result == 1:
                break

        else:
            player_2.append(arr[i])
            player_2_sorted = sorted(player_2)
            player_2_set = list(set(player_2_sorted))
            for j in range(len(player_2_sorted) - 2):
                if player_2_sorted[j] == player_2_sorted[j + 1] == player_2_sorted[j + 2]:
                    result = 2
                    break
            for j in range(len(player_2_set) - 2):
                if player_2_set[j] + 1 == player_2_set[j + 1] and player_2_set[j + 1] + 1 == player_2_set[j + 2]:
                    result = 2
                    break

            if result == 2:
                break

    print(f'#{tc} {result}')
