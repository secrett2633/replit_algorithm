n = list(input())
n.sort()
g = len(n)
sum = 0
finish = []
for i in range(len(n)):
    sum += int(n[i])
if sum % 3 != 0 or "0" not in n:
    print("-1")
else:
    if "0" in n:
        for i in range(g):
            finish.append(n[g-i-1])
    for i in range(g):
        print(finish[i], end="")