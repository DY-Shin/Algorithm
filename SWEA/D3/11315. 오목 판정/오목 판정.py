T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    result = 'NO'

    for j in range(N):
        for i in range(N - 4):
            flag = 1
            for k in range(5):
                if arr[i + k][j] != 'o':
                    flag = 0
                    break
            if flag:
                result = 'YES'

    for i in range(N - 4):
        for j in range(N - 4):
            flag = 1
            for k in range(5):
                if arr[i + k][j + k] != 'o':
                    flag = 0
                    break
            if flag:
                result = 'YES'

    for i in range(N):
        for j in range(N - 4):
            if arr[i][j] == 'o':
                if arr[i][j:j + 5] == ['o'] * 5:
                    result = 'YES'
                    break

    for i in range(4, N):
        for j in range(N - 4):
            flag = 1
            for k in range(5):
                if arr[i - k][j + k] != 'o':
                    flag = 0
                    break
            if flag:
                result = 'YES'

    print(f'#{test_case} {result}')
