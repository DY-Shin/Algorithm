import copy


def func(arr, n):
    table = []
    result = []
    ans = []
    for i in range(n):
        table.append(str(i))
    for i in range(len(arr)):
        for j in range(n):
            if arr[i] != table[j]:
                new_arr = copy.deepcopy(arr)
                new_arr[i] = table[j]
                result.append(''.join(new_arr))

    for i in range(len(result)):
        calc = 0
        for j in range(len(result[i])):
            calc += int(result[i][j]) * (n**(len(result[i]) - j - 1))
        ans.append(calc)
    return ans


T = int(input())
for test_case in range(1, T + 1):
    bin_num = list(map(str, input()))
    tri_num = list(map(str, input()))
    bin_ans = func(bin_num, 2)
    tri_ans = func(tri_num, 3)
    for i in bin_ans:
        if i in tri_ans:
            print(f'#{test_case} {i}')
