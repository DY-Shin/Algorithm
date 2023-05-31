import sys
input = sys.stdin.readline

result = 0
tmp = 0
for i in range(4):
    n, m = map(int, input().split())
    tmp += (m - n)
    result = max(tmp, result)
print(result)
