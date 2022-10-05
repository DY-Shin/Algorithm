from collections import deque
import copy


def BFS():
    global ans
    q = deque()
    new_arr = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if new_arr[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if new_arr[nx][ny] == 0:
                    new_arr[nx][ny] = 2
                    q.append((nx, ny))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if new_arr[i][j] == 0:
                cnt += 1
    ans = max(cnt, ans)


def wall(cnt):
    if cnt == 3:
        BFS()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt + 1)
                arr[i][j] = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
wall(0)
print(ans)
