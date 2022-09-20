bin_hex = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
           '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
           'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

secret = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    password = []
    result = []
    ans = 0
    for _ in range(N):
        bin_num = ''
        temp = input().strip()
        for j in range(len(temp)):
            bin_num += bin_hex[temp[j]]
        arr.append(bin_num)

    for i in range(1, N):
        j = M * 4 - 1
        while j > 55:
            if arr[i][j] != '0' and arr[i - 1][j] == '0':
                cnt1 = cnt2 = cnt3 = 0
                while arr[i][j - cnt1] != '0':
                    cnt1 += 1
                while arr[i][j - cnt1 - cnt2] != '1':
                    cnt2 += 1
                while arr[i][j - cnt1 - cnt2 - cnt3] != '0':
                    cnt3 += 1
                k_rate = [cnt3, cnt2, cnt1]
                k = min(k_rate)
                password.append([arr[i][j - 55 * k:j + 1], k])
                j -= 56 * k
            else:
                j -= 1

    for i in range(len(password)):
        rate = password[i][1]
        bin_pass = ''
        dec_num = ''
        for j in range(0, 56 * rate, rate):
            bin_pass += password[i][0][j]
        for k in range(0, len(bin_pass), 7):
            for l in range(10):
                if bin_pass[k:k+7] == secret[l]:
                    dec_num += str(l)
        result.append(dec_num)

    for i in range(len(result)):
        odd = even = 0
        for j in range(len(result[i])):
            if j % 2:
                even += int(result[i][j])
            else:
                odd += int(result[i][j])
        ssum = odd * 3 + even
        if ssum % 10 == 0:
            ans += (odd + even)

    print(f'#{test_case} {ans}')