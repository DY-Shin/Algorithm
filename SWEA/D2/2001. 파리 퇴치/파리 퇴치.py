T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cut = -1

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            cut = 0
            for k in range(M):
                for l in range(M):
                    cut += arr[i + k][j + l]
            if cut > max_cut:
                max_cut = cut

    print(f'#{test_case} {max_cut}')