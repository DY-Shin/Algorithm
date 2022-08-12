T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    total = 0
    cnt = 0

    for i in range(N):
        total += arr[i]

    average = total // N

    for i in range(N):
        if arr[i] <= average:
            cnt += 1

    print(f'#{test_case} {cnt}')