T = int(input())
for test_case in range(1, T + 1):
    case, strN = input().split()
    N = int(strN)
    gns = list(map(str, input().split()))
    arr = [0] * 10
    gns_dict = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    gns_list = []

    for i in range(N):
        for j in range(10):
            if gns[i] == gns_dict[j]:
                arr[j] += 1

    for i in range(10):
        for _ in range(arr[i]):
            gns_list.append(gns_dict[i])

    gns_output = ' '.join(gns_list)

    print(case, gns_output)