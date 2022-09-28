N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
print(round(sum(arr) / N))
print(arr[N // 2])
count = []
for i in range(-4000, 4001):
    count.append([i, 0])
for num in arr:
    count[num + 4000][1] += 1
count.sort(key=lambda x: (-x[1], x[0]))
if N == 1:
    print(arr[0])
else:
    if count[0][1] != count[1][1]:
        print(count[0][0])
    else:
        print(count[1][0])
print(max(arr) - min(arr))
