from collections import deque
import sys
input = sys.stdin.readline


def bfs(n):
    que = deque()
    que.append(n)
    while que:
        x = que.popleft()

        if x == K:
            return visited[x]

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < 100001:
                if not visited[nx]:
                    if nx == x * 2 and nx != 0:
                        visited[nx] = visited[x]
                        que.appendleft(nx)
                    else:
                        visited[nx] = visited[x] + 1
                        que.append(nx)


N, K = map(int, input().split())
visited = [0] * 100001
answer = bfs(N)
print(answer)
