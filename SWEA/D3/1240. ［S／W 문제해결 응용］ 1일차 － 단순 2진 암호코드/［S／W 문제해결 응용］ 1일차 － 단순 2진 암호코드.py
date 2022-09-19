T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    bin_pass = ['0001101', '0011001', '0010011', '0111101', '0100011',
                '0110001', '0101111', '0111011', '0110111', '0001011']
    num = []
    odd = 0
    even = 0
    flag = 1
    for _ in range(N):
        arr = input()
        if flag:
            for i in range(M - 1, 55, -1):
                if arr[i] == '1':
                    password = arr[i - 55:i + 1]
                    flag = 0
                    break
 
    for i in range(0, 56, 7):
        result = password[i:i + 7]
        for j in range(10):
            if result == bin_pass[j]:
                num.append(j)
    for i in range(8):
        if i % 2:
            even += num[i]
        else:
            odd += num[i]
    test = odd * 3 + even
    print(f'#{test_case}', end=' ')
    if test % 10:
        print(0)
    else:
        print(odd + even)