arr = [i for i in range(1, 11)]

def dfs(cnt = 0, total = 0, subset = []):

    if total == 10:
        print(subset)
        return

    if total > 10:
        return

    if cnt == 10:
        return

    dfs(cnt + 1, total, subset)  # 포함안하는경우
    dfs(cnt + 1, total + arr[cnt], subset + [arr[cnt]])  # 포함하는경우

dfs()





