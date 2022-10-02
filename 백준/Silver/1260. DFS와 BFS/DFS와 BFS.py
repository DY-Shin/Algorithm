from collections import deque


def DFS(v):
    visited_D[v] = 1
    print(v, end=' ')
    for w in adj_list[v]:
        if visited_D[w] == 0:
            visited_D[w] = 1
            DFS(w)


def BFS(v):
    q = deque()
    q.append(v)
    visited_B[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for w in adj_list[v]:
            if visited_B[w] == 0:
                q.append(w)
                visited_B[w] = visited_B[v] + 1


N, M, V = map(int, input().split())
visited_D = [0] * (N + 1)
visited_B = [0] * (N + 1)
adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)
for i in range(N + 1):
    adj_list[i].sort()
DFS(V)
print()
BFS(V)
