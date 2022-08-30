T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    cnt = 0

    for i in range(N // 2 + 1):
        for j in range(N // 2 + 1):
            if i + j >= N // 2:
                cnt += arr[i][j]

    for i in range(N // 2, N):
        for j in range(N // 2, N):
            if i + j < N + N // 2:
                cnt += arr[i][j]

    for i in range(N // 2, N):
        for j in range(N // 2 + 1):
            if j + N // 2 >= i:
                cnt += arr[i][j]

    for i in range(N // 2 + 1):
        for j in range(N // 2, N):
            if i + N // 2 >= j:
                cnt += arr[i][j]

    for i in range(N):
        for j in range(N):
            if i == N // 2:
                cnt -= arr[i][j]
            if j == N // 2:
                cnt -= arr[i][j]

    cnt -= arr[N//2][N//2]

    print(f'#{test_case} {cnt}')