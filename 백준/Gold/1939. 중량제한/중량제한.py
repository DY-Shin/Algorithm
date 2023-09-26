import sys
from collections import deque
input = sys.stdin.readline


def bfs(s, e, visited, mid):
    que = deque()
    que.append(s)
    while que:
        node = que.popleft()

        if node == e:
            return mid + 1

        for n in arr[node]:
            if n[1] >= mid and not visited[n[0]]:
                que.append(n[0])
                visited[n[0]] = 1

    return mid - 1


def binary(l, r):
    while l <= r:
        visited = [0 for _ in range(N + 1)]
        mid = (l + r) // 2
        new = bfs(s, e, visited, mid)
        if new == mid - 1:
            r = new
        elif new == mid + 1:
            l = new
    return r


N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
low = 0
high = 0
for i in range(M):
    A, B, C = map(int, input().split())
    arr[A].append([B, C])
    arr[B].append([A, C])
    high = max(high, C)
s, e = map(int, input().split())

result = binary(low, high)
print(result)
