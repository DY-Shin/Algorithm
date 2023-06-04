import sys
input = sys.stdin.readline

arr = []
for i in range(5):
    score = int(input())
    if score > 40:
        arr.append(score)
    else:
        arr.append(40)
result = sum(arr) // 5
print(result)
