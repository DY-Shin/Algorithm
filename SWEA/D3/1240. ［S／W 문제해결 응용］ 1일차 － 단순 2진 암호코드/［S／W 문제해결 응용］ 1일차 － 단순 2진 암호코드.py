T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    bin_pass = ['0001101', '0011001', '0010011', '0111101', '0100011',
                '0110001', '0101111', '0111011', '0110111', '0001011']
    result = []
    num = []
    k = 0
    l = 0
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j] == '1':
                password = arr[i][j - 55:j + 1]
                break

    for i in range(0, 56, 7):
        result.append(''.join(password[i:i + 7]))
    for i in range(8):
        for j in range(10):
            if result[i] == bin_pass[j]:
                num.append(j)
    for i in range(0, 8, 2):
        k += num[i]
    for i in range(1, 8, 2):
        l += num[i]
    test = k * 3 + l
    print(f'#{test_case}', end=' ')
    if test % 10:
        print(0)
    else:
        print(k + l)
