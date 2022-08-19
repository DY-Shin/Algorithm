T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    fac = [2, 3, 5, 7, 11]
    num = [0] * 5

    for i in range(5):
        while N % fac[i] == 0:
            N = N // fac[i]
            num[i] += 1

    print(f'#{test_case}', end=' ')
    print(*num)