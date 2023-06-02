import copy
from collections import deque


def bfs(r, c):
    q = deque()
    q.append((r, c))
    ch = arr[r][c]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == ch:
                q.append((nx, ny))
                visited[nx][ny] = 1


def bfs_red(r, c):
    q = deque()
    q.append((r, c))
    ch = arr_red[r][c]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited_red[nx][ny] and arr_red[nx][ny] == ch:
                q.append((nx, ny))
                visited_red[nx][ny] = 1


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
N = int(input())
arr = [list(input()) for _ in range(N)]
arr_red = copy.deepcopy(arr)
for i in range(N):
    for j in range(N):
        if arr_red[i][j] == 'G':
            arr_red[i][j] = 'R'
visited = [[0] * N for _ in range(N)]
visited_red = [[0] * N for _ in range(N)]
result = 0
result_red = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            result += 1
            bfs(i, j)
for i in range(N):
    for j in range(N):
        if not visited_red[i][j]:
            result_red += 1
            bfs_red(i, j)
print(result, result_red)
