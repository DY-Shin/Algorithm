import copy


def dfs(fish, x, y, arr):
    global total
    fish += arr[x][y][0]
    total = max(fish, total)
    arr[x][y][0] = 0
    fish_move(x, y, arr)
    for k in range(1, 4):
        nx = x + k * dx[arr[x][y][1]]
        ny = y + k * dy[arr[x][y][1]]
        if 0 <= nx < 4 and 0 <= ny < 4 and arr[nx][ny][0]:
            dfs(fish, nx, ny, copy.deepcopy(arr))


def fish_move(x, y, arr):
    for t in range(1, 17):
        fx, fy = -1, -1
        for i in range(4):
            for j in range(4):
                if arr[i][j][0] == t:
                    fx, fy = i, j
                    break
        if fx == -1 and fy == -1:
            continue
        fd = arr[fx][fy][1]

        for l in range(8):
            nd = (fd + l) % 8
            ni = fx + dx[nd]
            nj = fy + dy[nd]
            if not (0 <= ni < 4 and 0 <= nj < 4) or (ni == x and nj == y):
                continue
            arr[fx][fy][1] = nd
            arr[fx][fy], arr[ni][nj] = arr[ni][nj], arr[fx][fy]
            break


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
arr = [[] for _ in range(4)]
for i in range(4):
    inp = list(map(int, input().split()))
    for j in range(4):
        arr[i].append([inp[2 * j], inp[2 * j + 1] - 1])
total = 0
dfs(0, 0, 0, arr)
print(total)
