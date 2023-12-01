from collections import deque


def shark_check():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                return i, j


def bfs(r, c):
    visited = [[0] * N for _ in range(N)]
    que = deque()
    que.append((r, c))
    visited[r][c] = 1
    cand = []
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if arr[nx][ny] == shark or arr[nx][ny] == 0:
                    que.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                elif arr[nx][ny] < shark and arr[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    cand.append((visited[nx][ny] - 1, nx, ny))
    return sorted(cand, key=lambda o: (o[0], o[1], o[2]))


dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
shark = 2
cnt = 0
result = 0
while True:
    a, b = shark_check()
    cand = deque(bfs(a, b))

    if not cand:
        break

    step, na, nb = cand.popleft()
    result += step
    cnt += 1

    if cnt == shark:
        shark += 1
        cnt = 0

    arr[a][b] = 0
    arr[na][nb] = 9

print(result)
