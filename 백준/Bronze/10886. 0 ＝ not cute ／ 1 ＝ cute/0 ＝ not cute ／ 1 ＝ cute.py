N = int(input())
cute = "Junhee is cute!"
cute_count = 0
not_cute = "Junhee is not cute!"
not_cute_count = 0
for i in range(N):
    survey = int(input())
    if survey == 1:
        cute_count += 1
    else:
        not_cute_count += 1

if cute_count > not_cute_count:
    print(cute)
else:
    print(not_cute)