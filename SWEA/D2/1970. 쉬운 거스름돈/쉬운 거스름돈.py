T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    arr = []

    for i in money:
        cnt = N // i
        N -= cnt * i
        arr.append(cnt)

    print(f'#{test_case}')
    print(*arr)