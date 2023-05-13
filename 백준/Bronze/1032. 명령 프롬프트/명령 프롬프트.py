import sys
input = sys.stdin.readline

n = int(input())
result = list(map(str, input()))
for i in range(1, n):
    comp = list(map(str, input()))
    for j in range(len(result)):
        if result[j] != comp[j]:
            result[j] = '?'
print(''.join(result))
