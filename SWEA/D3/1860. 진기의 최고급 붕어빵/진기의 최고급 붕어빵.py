T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    bread = 0
    flag = 1
    if 0 in arr:
        flag = 0
    for i in range(1, max(arr) + 1):
        if not i % M:
            bread += K
        for j in arr:
            if j == i:
                bread -= 1
                if bread < 0:
                    flag = 0
                    break
    print(f'#{test_case}', end=' ')
    if flag:
        print('Possible')
    else:
        print('Impossible')