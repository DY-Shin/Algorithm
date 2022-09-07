N = int(input())
rope = [int(input()) for _ in range(N)]
rope.sort(reverse=True)
arr = []
for i in range(N):
    arr.append(rope[i] * (i + 1))
result = max(arr)

print(result)