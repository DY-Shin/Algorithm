T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    X = -1
    for i in range(1, 10**6 + 1):
        if N == i**3:
            X = i

    print(f'#{test_case} {X}')
