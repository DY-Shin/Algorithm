n, m = map(int, input().split())
pwd = dict()
for i in range(n):
    address, password = map(str, input().split())
    pwd[address] = password
for i in range(m):
    result = input()
    print(pwd[result])
