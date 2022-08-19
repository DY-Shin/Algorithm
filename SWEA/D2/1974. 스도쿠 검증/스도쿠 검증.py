T = int(input())
N = 9
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(N)]
    flag = 1

    for i in range(N):
        check = [0] * N
        for j in range(N):
            check[arr[i][j] - 1] += 1
        if 0 in check:
            flag = 0
            break

    for i in range(N):
        check = [0] * N
        for j in range(N):
            check[arr[j][i] - 1] += 1
        if 0 in check:
            flag = 0
            break

    for i in range(0, N, 3):
        check = [0] * N
        for j in range(0, N, 3):
            for k in range(3):
                for l in range(3):
                    check[arr[i + k][j + l] - 1] += 1
            if 0 in check:
                flag = 0
                break

    print(f'#{test_case} {flag}')