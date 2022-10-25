N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))
cnt = 1
i = 0
j = 1
while i < N - j:
    if arr[i + j][0] >= arr[i][1]:
        cnt += 1
        i += j
        j = 0
    j += 1
print(cnt)