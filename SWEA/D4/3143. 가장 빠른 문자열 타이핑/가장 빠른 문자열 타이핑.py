def BruteForce(t, p):
    cnt = 0
    i = 0
    while i < N - M + 1:
        flag = 1
        for j in range(M):
            if t[i + j] != p[j]:
                flag = 0
                i = i + 1
                break
        if flag:
            cnt += 1
            i = i + M
    return cnt

T = int(input())
for test_case in range(1, T + 1):
    text, pattern = map(str, input().split())
    N = len(text)
    M = len(pattern)

    pt_cnt = BruteForce(text, pattern)
    total = N - (pt_cnt * M) + pt_cnt

    print(f'#{test_case} {total}')