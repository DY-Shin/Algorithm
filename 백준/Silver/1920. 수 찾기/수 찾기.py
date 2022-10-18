def bin_search(m):
    left = 0
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        if N_list[mid] == m:
            return 1
        elif N_list[mid] > m:
            right = mid - 1
        else:
            left = mid + 1
    return 0


N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))
N_list.sort()
for i in range(M):
    print(bin_search(M_list[i]))