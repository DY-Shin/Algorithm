arr = input()
N = len(arr)
k = []

for i in range(N):
    for j in range(1, N - i + 1):
        k.append(arr[i:i+j])

set_k = set(k)
result = len(set_k)
print(result)