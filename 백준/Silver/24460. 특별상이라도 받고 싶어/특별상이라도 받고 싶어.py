def split(x, y, n):
    if n == 1:
        return arr[x][y]
    else:
        cut = [split(x, y, n // 2), split(x, y + (n // 2), n // 2),
               split(x + (n // 2), y, n // 2), split(x + (n // 2), y + (n // 2), n // 2)]
        cut.sort()
        return cut[1]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(split(0, 0, N))
