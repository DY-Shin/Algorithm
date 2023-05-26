num = int(input())
s = input()
for i in range(len(s) - 1, -1, -1):
    print(num * int(s[i]))
s = int(s)
print(num * s)
