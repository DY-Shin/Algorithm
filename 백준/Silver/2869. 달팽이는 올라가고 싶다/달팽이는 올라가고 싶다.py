A, B, V = map(int, input().split())
cnt = 0

V -= A
result = V // (A - B)
if V % (A-B):
    result += 2
else:
    result += 1

print(result)
