from itertools import combinations
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
x = [0] * N
y = [0] * N
answer = 987654321
for i in range(N):
    x[i], y[i] = map(int, input().split())

for c in combinations(range(N), K):
    case = 0
    for j in range(N):
        dis = 987654321
        for k in c:
            tmp = abs(x[j] - x[k]) + abs(y[j] - y[k])
            dis = min(tmp, dis)
        case = max(case, dis)
    answer = min(answer, case)
print(answer)
