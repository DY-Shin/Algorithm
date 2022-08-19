T = int(input())
for test_case in range(1, T + 1):
    stack = []
    text = input()
    total = 0
    i = 0

    while i < len(text):
        if text[i: i+2] == '()':
            stack.append(1)
            i += 1
        elif text[i] == '(':
            stack.append('(')
        else:
            n = stack.pop()
            tmp = 0
            while n != '(':
                tmp += n
                n = stack.pop()
            stack.append(tmp)
            total += (tmp + 1)
        i += 1

    print(f'#{test_case} {total}')