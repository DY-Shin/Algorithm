import sys
input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N):
    cmd = input().strip()
    if cmd == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif cmd == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    else:
        push, num = cmd.split()
        stack.append(num)
