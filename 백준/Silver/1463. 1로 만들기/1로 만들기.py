N = int(input())
cnt = 0
dp = [0] * (N + 1)
dp[1] = 0
if N > 1:
    dp[2] = 1
if N > 2:
    dp[3] = 1
for i in range(4, N + 1):
    tmp_2, tmp_3 = 987654321, 987654321
    if i % 2 == 0:
        tmp_2 = dp[i // 2] + 1
    if i % 3 == 0:
        tmp_3 = dp[i // 3] + 1
    tmp_list = [dp[i - 1] + 1, tmp_2, tmp_3]
    dp[i] = min(tmp_list)
print(dp[N])