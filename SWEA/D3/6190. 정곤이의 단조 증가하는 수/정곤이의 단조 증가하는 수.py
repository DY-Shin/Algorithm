T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = -1

    for i in range(N):
        for j in range(i + 1, N):
            tmp = arr[i] * arr[j]
            tmp_s = str(tmp)
            flag = 1
            for k in range(len(tmp_s) - 1):
                if tmp_s[k] > tmp_s[k + 1]:
                    flag = 0
                    break
            if flag:
                if tmp > result:
                    result = tmp

    print(f'#{test_case} {result}')