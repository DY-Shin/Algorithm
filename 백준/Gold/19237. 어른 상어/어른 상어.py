def first_shark():
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                shark_pos[arr[i][j] - 1] = [i, j]


def shark_move(shark):
    x, y = shark_pos[shark][0], shark_pos[shark][1]

    if x == -1 and y == -1:
        tmp_shark.append([-1, -1])
        return

    dir = shark_dir[shark]
    for k in range(4):
        dpr = shark_pri[shark][dir - 1][k]
        nx = x + dx[dpr - 1]
        ny = y + dy[dpr - 1]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            shark_dir[shark] = dpr
            tmp_shark.append([nx, ny])
            break
    else:
        for k in range(4):
            dpr = shark_pri[shark][dir - 1][k]
            nx = x + dx[dpr - 1]
            ny = y + dy[dpr - 1]
            if 0 <= nx < N and 0 <= ny < N:
                if visited_s[nx][ny] == shark + 1:
                    shark_dir[shark] = dpr
                    tmp_shark.append([nx, ny])
                    break


def visit():
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                visited[i][j] -= 1
            else:
                visited_s[i][j] = 0

            if arr[i][j]:
                visited[i][j] = K
                visited_s[i][j] = arr[i][j]


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 1:위 2:아래 3:왼쪽 4:오른쪽
shark_dir = list(map(int, input().split()))
# 위, 아래, 왼쪽, 오른쪽을 향할 때 우선순위
shark_pri = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * N for _ in range(N)]
visited_s = [[0] * N for _ in range(N)]
shark_pos = [[] for _ in range(M)]
first_shark()
sharks = M - 1
result = 0
while sharks:
    tmp_shark = []
    visit()
    for i in range(M):
        shark_move(i)
    tmp_arr = [[0] * N for _ in range(N)]
    for i in range(M):
        if tmp_shark[i][0] == -1 and tmp_shark[i][1] == -1:
            continue
        if not tmp_arr[tmp_shark[i][0]][tmp_shark[i][1]]:
            tmp_arr[tmp_shark[i][0]][tmp_shark[i][1]] = i + 1
            shark_pos[i] = tmp_shark[i]
        else:
            shark_pos[i] = [-1, -1]
            sharks -= 1
    arr = tmp_arr
    result += 1
    if result > 1000:
        result = -1
        break
print(result)
