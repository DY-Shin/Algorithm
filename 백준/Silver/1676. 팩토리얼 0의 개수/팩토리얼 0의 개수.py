import sys
input = sys.stdin.readline

N = int(input())
number = 1
for i in range(1, N + 1):
    number *= i
num = str(number)
result = 0
for i in range(len(num) - 1, -1, -1):
    if num[i] == '0':
        result += 1
    else:
        break
print(result)
