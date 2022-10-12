N = int(input())
dasom = int(input())
arr = []
for _ in range(N - 1):
    arr.append(int(input()))
cnt = 0
if arr:
    while dasom < max(arr):
        for i in range(N - 1):
            if arr[i] == max(arr):
                arr[i] -= 1
                dasom += 1
                cnt += 1
                break
    if dasom == max(arr):
        cnt += 1
print(cnt)