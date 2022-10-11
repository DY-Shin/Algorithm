N = input()
arr = [str(i) for i in range(10)]
q = [0] * 10
for i in range(len(N)):
    q[int(N[i])] += 1
if (q[6] + q[9]) % 2:
    q[6] = (q[6] + q[9]) // 2 + 1
    q[9] = 0
else:
    q[6] = (q[6] + q[9]) // 2
    q[9] = 0
print(max(q))