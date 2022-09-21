def DFS(v, cnt):
    visited[v] = 1
    for w in tree[v]:
        if visited[w] == 0:
            cnt = DFS(w, cnt + 1)
    return cnt


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    tree = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    print(DFS(1, 0))
