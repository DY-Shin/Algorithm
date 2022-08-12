T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [0] * 10

    for i in range(10000000):
        sheep = N * i
        while sheep:
            arr[sheep % 10] = 1
            sheep //= 10
        if 0 not in arr:
            sheepnum = i
            break

    print(f'#{test_case} {N * sheepnum}')