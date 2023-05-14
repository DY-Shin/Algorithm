t = int(input())
for _ in range(t):
    p = int(input())
    player_list = []
    for i in range(p):
        c, name = input().split()
        c = int(c)
        player_list.append((c, name))
    player_list.sort()
    print(player_list[-1][1])