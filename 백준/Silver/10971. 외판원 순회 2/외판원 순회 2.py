def DFS(x, cnt, money):
    global ans
    global start
    if money > ans:
        return

    if cnt == N - 1:
        if W[x][start] != 0:
            ans = min(ans, money + W[x][start])
        return

    for i in range(N):
        if W[x][i] != 0 and i != start and not visited[i]:
            visited[i] = 1
            DFS(i, cnt + 1, money + W[x][i])
            visited[i] = 0


N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
ans = 987654321
for i in range(N):
    start = i
    DFS(i, 0, 0)
print(ans)