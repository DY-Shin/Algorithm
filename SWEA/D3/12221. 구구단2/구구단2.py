T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    print(f'#{test_case}', end=' ')
    if N > 9 or M > 9:
        print(-1)
    else:
        print(N * M)
        