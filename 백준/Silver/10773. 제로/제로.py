N = int(input())
arr = []
for i in range(N):
    value = int(input())
    if value == 0:
        arr.pop()
    else:
        arr.append(value)
print(sum(arr))