def DFS(v):
    visited[v] = 1
    for w in adj_list[v]:
        if visited[w] == 0:
            DFS(w)

T = 10
V = 100
S, G = 0, 99
for test_case in range(1, T + 1):
    case, E = map(int, input().split())
    temp = list(map(int, input().split()))
    adj_list = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for i in range(E):
        s, e = temp[2 * i], temp[2 * i + 1]
        adj_list[s].append(e)

    DFS(S)

    print(f'#{case} {visited[G]}')