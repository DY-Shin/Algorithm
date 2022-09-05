while True:
    arr = list(map(str, input()))
    if arr[0] == '.':
        break
    stack = []
    result = 'yes'
    for i in arr:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    result = 'no'
                    break
            else:
                result = 'no'
                break
        elif i == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    result = 'no'
                    break
            else:
                result = 'no'
                break
        elif i == '.':
            stack.append(i)
            break
    if len(stack) > 1:
        result = 'no'
    print(result)