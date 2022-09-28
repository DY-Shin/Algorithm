from collections import deque

N = int(input())
Q = deque()
for i in range(1, N + 1):
    Q.append(i)
while len(Q) > 1:
    Q.popleft()
    if len(Q) > 1:
        num = Q.popleft()
        Q.append(num)
    else:
        break
print(Q[0])