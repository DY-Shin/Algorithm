T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cnt = [0] * 5001
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B + 1):
            cnt[j] += 1
    P = int(input())
    print(f'#{test_case}', end=' ')
    for i in range(P):
        C = int(input())
        print(cnt[C], end=' ')
    print()
