N = int(input())
arr = [str(i) for i in range(1, N + 1)]
cnt = 0
for i in range(N):
    if len(arr[i]) <= 2:
        cnt += 1
    else:
        flag = 1
        for j in range(len(arr[i]) - 2):
            if int(arr[i][j + 1]) - int(arr[i][j]) != int(arr[i][j + 2]) - int(arr[i][j + 1]):
                flag = 0
                break
        if flag:
            cnt += 1
print(cnt)