T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    N_str = str(N)
    result = (' 1/' + N_str) * N

    print(f'#{test_case}{result}')