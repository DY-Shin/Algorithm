T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = list(map(int, input().split()))
    max_tree = max(tree)
    op = 0
    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        k = max_tree - tree[i]
        op += k
        if k == 1 or k % 2:
            cnt1 += 1
        while k > 1:
            k -= 2
            cnt2 += 1
    if op < 3:
        ans = op
    else:
        if cnt2 >= cnt1 - 1:
            ans = op - op // 3
        else:
            ans = cnt1 * 2 - 1
    print(f'#{tc} {ans}')