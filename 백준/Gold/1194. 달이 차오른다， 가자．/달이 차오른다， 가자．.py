import sys
from collections import deque


def bfs():
    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '0':
                q.append((i, j, 0, 0))
                visited[i][j] = 0
                arr[i][j] = '.'
                break
        else:
            continue
        break

    while q:
        x, y, cnt, bit = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0 or arr[nx][ny] == '#':
                continue

            if not visited[nx][ny] == -1 and visited[nx][ny] | bit == visited[nx][ny]:
                continue
            visited[nx][ny] = bit

            if visited[nx][ny] == -1:
                visited[nx][ny] = 0

            if arr[nx][ny] == '.':
                q.append((nx, ny, cnt + 1, bit))
                continue

            if arr[nx][ny] == '1':
                print(cnt + 1)
                sys.exit()

            k = key.get(arr[nx][ny])
            if k != None:
                q.append((nx, ny, cnt + 1, bit | k))
                continue

            d = door.get(arr[nx][ny])
            if d | bit == bit:
                q.append((nx, ny, cnt + 1, bit))

    print(-1)


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
key = {'a': 1, 'b': 2, 'c': 4, 'd': 8, 'e': 16, 'f': 32}
door = {'A': 1, 'B': 2, 'C': 4, 'D': 8, 'E': 16, 'F': 32}
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
bfs()
