N_arr = list(map(str, input()))
F = int(input())
N_arr[-1] = '0'
N_arr[-2] = '0'
new_N = int(''.join(N_arr))
mod = new_N % F
if mod == 0:
    print('00')
elif (F - mod) < 10:
    print('0' + f'{F - mod}')
else:
    print(F - mod)
