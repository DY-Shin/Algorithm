def DFS(x, y, result):
    if len(result) == 7:
        ans_list.add(result)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                DFS(nx, ny, result + str(arr[x][y]))


dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    ans_list = set()
    for i in range(4):
        for j in range(4):
            DFS(i, j, '')

    print(f'#{test_case} {len(ans_list)}')