di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    i = j = k = 0
    num = 1
    while num <= N * N:
        arr[i][j] = num
        num += 1
        i += di[k]
        j += dj[k]
        if i < 0 or i >= N or j < 0 or j >= N or arr[i][j] != 0:
            i -= di[k]
            j -= dj[k]
            k = (k + 1) % 4
            i += di[k]
            j += dj[k]

    print(f'#{test_case}')
    for i in arr:
        print(*i)
