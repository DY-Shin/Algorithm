N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
result = 0
for i in range(N):
    if A[i] > B:
        k = A[i] - B
        if k % C:
            tmp = k // C + 1
        else:
            tmp = k // C
        result += tmp + 1
    else:
        result += 1

print(result)