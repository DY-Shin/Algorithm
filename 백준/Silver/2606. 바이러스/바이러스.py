from collections import deque
import sys
input = sys.stdin.readline


def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        n = q.popleft()
        for w in adj_list[n]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1


N = int(input())
E = int(input())
adj_list = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for i in range(E):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)
bfs(1)
print(sum(visited) - 1)
