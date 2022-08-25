from collections import deque

def sfind(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

def efind(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                return i, j

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    if arr[x][y] == 3:
        return

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx == N:
                continue
            if ny < 0 or ny == N:
                continue
            if visited[nx][ny]:
                continue
            if arr[nx][ny] == 1:
                continue
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = 10
for test_case in range(1, T + 1):
    case = int(input())
    N = 100
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    sx, sy = sfind(arr)
    bfs(sx, sy)
    ex, ey = efind(arr)
    result = visited[ex][ey]
    if result > 0:
        result = 1
    print(f'#{test_case} {result}')
