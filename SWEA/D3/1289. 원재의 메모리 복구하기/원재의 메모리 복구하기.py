T = int(input())
for test_case in range(1, T + 1):

    org_list = list(map(int, input()))
    N = len(org_list)
    arr = [0] * N
    cnt = 0

    for i in range(N):
        if arr[i] != org_list[i] and org_list[i] == 0:
            cnt += 1
            for j in range(i, N):
                arr[j] = 0
        elif arr[i] != org_list[i] and org_list[i] == 1:
            cnt += 1
            for j in range(i, N):
                arr[j] = 1
        elif arr == org_list:
            break

    print(f'#{test_case} {cnt}')