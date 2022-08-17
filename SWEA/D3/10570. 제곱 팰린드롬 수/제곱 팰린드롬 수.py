T = int(input())
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    cnt = 0

    for i in range(B + 1):
        if str(i) == str(i)[::-1]:
            double = i ** 2
            if str(double) == str(double)[::-1] and A <= double <= B:
                cnt += 1

    print(f'#{test_case} {cnt}')