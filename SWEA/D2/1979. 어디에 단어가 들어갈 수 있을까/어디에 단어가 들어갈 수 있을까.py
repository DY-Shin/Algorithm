T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    voca_list = [1] * K
    cnt = 0

    for i in range(N):
        for j in range(N - K + 1):
            flag = 1
            for k in range(K):
                if arr[i][j + k] != voca_list[k]:
                    flag = 0
                    break
                elif j + k != N - 1 and k == K - 1:
                    if arr[i][j + k + 1] == 1:
                        flag = 0
                        break
                elif j + k != 0 and k == 0:
                    if arr[i][j + k - 1] == 1:
                        flag = 0
                        break
            if flag:
                cnt += 1

    for i in range(N - K + 1):
        for j in range(N):
            flag = 1
            for k in range(K):
                if arr[i + k][j] != voca_list[k]:
                    flag = 0
                    break
                elif i + k != N - 1 and k == K - 1:
                    if arr[i + k + 1][j] == 1:
                        flag = 0
                        break
                elif i + k != 0 and k == 0:
                    if arr[i + k - 1][j] == 1:
                        flag = 0
                        break
            if flag:
                cnt += 1

    print(f'#{test_case} {cnt}')