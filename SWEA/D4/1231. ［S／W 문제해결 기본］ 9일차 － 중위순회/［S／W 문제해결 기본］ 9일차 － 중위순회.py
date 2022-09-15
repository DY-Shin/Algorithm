def inorder(n):
    global ans
    if n <= N:
        inorder(n * 2)
        ans += tree[n]
        inorder(n * 2 + 1)


T = 10
for test_case in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    for _ in range(N):
        temp = input().split()
        tree[int(temp[0])] = temp[1]
    ans = ''
    inorder(1)
    print(f'#{test_case} {ans}')
