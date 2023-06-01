import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
for i in range(N):
    A = int(input())
    arr.append(A)
i = N - 1
result = 0
while K > 0:
    if K >= arr[i]:
        tmp = K // arr[i]
        K -= arr[i] * tmp
        result += tmp
    else:
        i -= 1
print(result)
