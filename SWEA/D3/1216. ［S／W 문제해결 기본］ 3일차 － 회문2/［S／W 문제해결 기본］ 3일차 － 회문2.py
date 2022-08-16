T = 10
for test_case in range(1, T + 1):
    case = int(input())
    N = 100
    arr = [list(map(str, input())) for _ in range(N)]
    lth = 0

    for i in range(N):
        for j in range(N - 1):
            for k in range(2, N - j + 1):
                flag_r = 1
                flag_c = 1
                for l in range(k // 2):
                    if arr[i][j + l] != arr[i][j + k - 1 - l]:
                        flag_r = 0
                        break
                for l in range(k // 2):
                    if arr[j + l][i] != arr[j + k - 1 - l][i]:
                        flag_c = 0
                        break
                if flag_r or flag_c:
                    if k > lth:
                        lth = k

    print(f'#{case} {lth}')