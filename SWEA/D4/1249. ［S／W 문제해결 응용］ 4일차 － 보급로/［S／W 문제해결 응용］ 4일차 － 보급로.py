import heapq


def dijkstra(x, y):
    heap = []
    D[x][y] = 0
    heapq.heappush(heap, (D[x][y], x, y))
    while heap:
        d, x, y = heapq.heappop(heap)
        visited[x][y] = 1
        if x == N - 1 and y == N - 1:
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if D[nx][ny] > D[x][y] + arr[nx][ny]:
                    D[nx][ny] = D[x][y] + arr[nx][ny]
                    heapq.heappush(heap, (D[nx][ny], nx, ny))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = 987654321
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    D = [[INF] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dijkstra(0, 0)
    print(f'#{test_case} {D[N - 1][N - 1]}')
