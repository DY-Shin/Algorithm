import sys
input = sys.stdin.readline

M = int(input())
S = [0] * 21
for i in range(M):
    inp = input().strip()
    if inp == "all":
        for j in range(21):
            S[j] = 1
    elif inp == "empty":
        for j in range(21):
            S[j] = 0
    else:
        calc, num = map(str, inp.split())
        num = int(num)
        if calc == "add":
            S[num] = 1
        elif calc == "check":
            print(S[num])
        elif calc == "remove":
            S[num] = 0
        elif calc == "toggle":
            if S[num] == 0:
                S[num] = 1
            else:
                S[num] = 0
