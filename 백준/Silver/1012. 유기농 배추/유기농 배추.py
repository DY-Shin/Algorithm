import sys
sys.setrecursionlimit(10**6)


def DFS(x, y):
    global cnt
    if visited[x][y]:
        return

    visited[x][y] = 1
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] and not visited[nx][ny]:
                DFS(nx, ny)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for test_case in range(1, T + 1):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for k in range(K):
        j, i = map(int, input().split())
        arr[i][j] = 1
    visited = [[0]*M for _ in range(N)]
    worm = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            if arr[i][j]:
                DFS(i, j)
                if cnt != 0:
                    worm += 1
    print(worm)