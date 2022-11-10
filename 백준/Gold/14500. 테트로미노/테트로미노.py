def DFS(x, y, num, cnt):
    global ans

    if cnt == 4:
        ans = max(ans, num)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = 1
            DFS(nx, ny, num + arr[nx][ny], cnt + 1)
            visited[nx][ny] = 0


from itertools import combinations
N, M = map(int, input().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        DFS(i, j, arr[i][j], 1)
        visited[i][j] = 0
        for c in combinations(range(4), 3):
            temp = arr[i][j]
            for k in c:
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < N and 0 <= nj < M:
                    temp += arr[ni][nj]
                else:
                    break
            ans = max(ans, temp)
print(ans)
