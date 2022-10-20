def paper(x, y, n):
    global white, blue
    cnt = 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j]:
                cnt += 1
    if not cnt:
        white += 1
    elif cnt == n ** 2:
        blue += 1
    else:
        paper(x, y, n // 2)
        paper(x + n // 2, y, n // 2)
        paper(x, y + n // 2, n // 2)
        paper(x + n // 2, y + n // 2, n // 2)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0
paper(0, 0, N)
print(white)
print(blue)