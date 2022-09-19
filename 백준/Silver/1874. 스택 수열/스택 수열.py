n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
result = []
i = 1
cnt = 0

while cnt < n:
    if i > n + 1:
        result = ['NO']
        break
    else:
        if stack:
            if stack[-1] == arr[cnt]:
                stack.pop()
                result.append('-')
                cnt += 1
            else:
                stack.append(i)
                result.append('+')
                i += 1
        else:
            stack.append(i)
            result.append('+')
            i += 1

for i in range(len(result)):
    print(result[i])
