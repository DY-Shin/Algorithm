T = 10
for test_case in range(1, T + 1):
    N, password = input().split()
    N = int(N)
    stack = []

    for i in range(len(password)):
        if stack:
            if stack[-1] == password[i]:
                stack.pop()
            else:
                stack.append(password[i])
        else:
            stack.append(password[i])

    result = ''.join(stack)
    print(f'#{test_case} {result}')