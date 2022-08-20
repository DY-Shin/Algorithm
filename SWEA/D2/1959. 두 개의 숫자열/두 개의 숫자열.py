T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0

    if N < M:
        for i in range(M - N + 1):
            total = 0
            for j in range(N):
                total += A[j] * B[i + j]
            if total > result:
                result = total
    else:
        for i in range(N - M + 1):
            total = 0
            for j in range(M):
                total += A[i + j] * B[j]
            if total > result:
                result = total

    print(f'#{test_case} {result}')