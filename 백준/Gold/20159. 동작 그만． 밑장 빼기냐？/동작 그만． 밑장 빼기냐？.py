N = int(input())
X = list(map(int, input().split()))

origin = 0
for i in range(N):
    if not i % 2:
        origin += X[i]

result = origin

total_a = origin
for i in range(N - 1, 0, -2):
    total_a += X[i]
    total_a -= X[i - 1]
    result = max(total_a, result)

total_b = origin
for i in range(N - 2, 1, -2):
    total_b -= X[i]
    total_b += X[i - 1]
    result = max(total_b, result)

print(result)
