def sugar(num):
    i = 0
    j = 0
    arr = []
    while i >= 0:
        while j >= 0:
            k = 5 * i + 3 * j
            if num == k:
                arr.append([i, j])
            elif num < k:
                j = 0
                break
            j += 1
        if num < 5 * i:
            break
        i += 1
    if len(arr) == 0:
        result = -1
    else:
        result = arr[-1][0] + arr[-1][1]

    return result

N = int(input())

print(sugar(N))