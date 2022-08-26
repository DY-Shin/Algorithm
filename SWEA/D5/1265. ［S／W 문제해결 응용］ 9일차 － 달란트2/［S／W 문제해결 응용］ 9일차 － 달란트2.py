T = int(input())
for test_case in range(1, T + 1):
    N, P = map(int, input().split())
    tmp = N // P
    mod = N % P

    if mod:
        result = tmp ** (P - mod) * (tmp + 1) ** (mod)
    else:
        result = tmp ** P

    print(f'#{test_case} {result}')