import sys
input = sys.stdin.readline

sen = input().rstrip()
pattern = input().rstrip()

stack = []
p_len = len(pattern)

for i in range(len(sen)):
    stack.append(sen[i])
    if "".join(stack[-p_len:]) == pattern:
        for _ in range(p_len):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")
