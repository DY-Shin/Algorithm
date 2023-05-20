from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                q.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1


M, N = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
bfs()
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print(-1)
            exit()
        if arr[i][j] > result:
            result = arr[i][j]
print(result - 1)
