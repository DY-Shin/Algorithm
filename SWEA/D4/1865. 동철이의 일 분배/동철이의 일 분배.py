def perm(n, k, max_v):
    global ans
    if ans >= max_v:
        return

    if n == k:
        if ans < max_v:
            ans = max_v
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                p[k] = a[i]
                perm(n, k + 1, max_v * (arr[k][p[k]] / 100))
                visited[i] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    p = [0] * N
    a = list(range(N))
    ans = 0
    perm(N, 0, 1)
    print('#%d %f' % (test_case, ans * 100))
