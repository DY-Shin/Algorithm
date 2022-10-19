def comb(n, r, k, s):
    if k == r:
        print(*t)
    else:
        for i in range(s, n - r + 1 + k):
            t[k] = arr[i]
            comb(n, r, k + 1, i + 1)


N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
t = [0] * M
comb(N, M, 0, 0)