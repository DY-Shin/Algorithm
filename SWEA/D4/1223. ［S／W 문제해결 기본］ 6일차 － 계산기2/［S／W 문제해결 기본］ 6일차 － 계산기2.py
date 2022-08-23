T = 10
for test_case in range(1, T + 1):
    N = int(input())
    expression = input()
    stack = []
    result = []
    isp = {'*': 2, '+': 1}
    icp = {'*': 2, '+': 1}

    for i in range(N):
        if expression[i].isdecimal():
            result.append(expression[i])
        else:
            if stack:
                n = stack[-1]
                while isp[n] >= icp[expression[i]]:
                    result.append(stack.pop())
                    if stack:
                        n = stack[-1]
                    else:
                        break
                stack.append(expression[i])
            else:
                stack.append(expression[i])

    while stack:
        result.append(stack.pop())

    for i in result:
        if i.isdecimal():
            stack.append(int(i))
        else:
            k2 = stack.pop()
            k1 = stack.pop()
            if i == '*':
                stack.append(k1 * k2)
            elif i == '+':
                stack.append(k1 + k2)
    print(f'#{test_case} {stack[0]}')