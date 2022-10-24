from collections import deque

N, M = map(int, input().split())
arr = list(map(int, input().split()))
q = [i for i in range(1, N + 1)]
q = deque(q)
result = 0
for i in range(M):
    while q:
        if arr[i] == q[0]:
            q.popleft()
            break
        elif q.index(arr[i]) <= (N - i - 1) // 2:
            tmp = q.popleft()
            q.append(tmp)
            result += 1
        else:
            tmp = q.pop()
            q.insert(0, tmp)
            result += 1

print(result)