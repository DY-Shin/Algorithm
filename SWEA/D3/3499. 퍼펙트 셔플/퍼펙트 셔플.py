T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    hearth = list(map(str, input().split()))
    stone = [0] * N

    for i in range(N):
        if i < (N + 1) // 2:
            stone[2 * i] = hearth[i]
        else:
            for j in range(N // 2):
                stone[2 * j + 1] = hearth[(N + 1) // 2 + j]

    print(f'#{test_case}', end=' ')
    print(*stone)