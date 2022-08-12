def Bruteforce(t, p):
    total = 0
    for i in range(N - M + 1):
        flag = 1
        for j in range(M):
            if t[i + j] != p[j]:
                flag = 0
                break
        if flag:
            total += 1
    return total

T = 10
for test_case in range(1, T + 1):
    case = int(input())
    pattern = input()
    text = input()
    N = len(text)
    M = len(pattern)

    print(f'#{case} {Bruteforce(text, pattern)}')