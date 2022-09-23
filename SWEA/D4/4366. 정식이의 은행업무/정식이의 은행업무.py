import copy

T = int(input())
for test_case in range(1, T + 1):
    bin_num = list(map(str, input()))
    tri_num = list(map(str, input()))
    bin_table = ['0', '1']
    tri_table = ['0', '1', '2']
    bin_result = []
    tri_result = []
    bin_ans = []
    tri_ans = []
    for i in range(len(bin_num)):
        for j in range(2):
            if bin_num[i] != bin_table[j]:
                new_bin = copy.deepcopy(bin_num)
                new_bin[i] = bin_table[j]
                bin_result.append(''.join(new_bin))

    for i in range(len(tri_num)):
        for j in range(3):
            if tri_num[i] != tri_table[j]:
                new_tri = copy.deepcopy(tri_num)
                new_tri[i] = tri_table[j]
                tri_result.append(''.join(new_tri))

    for i in range(len(tri_result)):
        calc = 0
        for j in range(len(tri_result[i])):
            calc += int(tri_result[i][j]) * (3**(len(tri_result[i]) - j - 1))
        tri_ans.append(calc)
    for i in range(len(bin_result)):
        bin_ans.append(int('0b' + bin_result[i], 2))

    for i in bin_ans:
        if i in tri_ans:
            print(f'#{test_case} {i}')