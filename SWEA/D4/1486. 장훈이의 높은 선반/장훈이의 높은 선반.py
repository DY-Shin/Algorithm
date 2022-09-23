T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    people = list(map(int, input().split()))
    result = []
    for i in range(1, 1 << N):
        part_list = []
        for j in range(N):
            if i & (1 << j):
                part_list.append(people[j])
        if sum(part_list) >= B:
            result.append(sum(part_list))

    print(f'#{test_case} {min(result) - B}')
