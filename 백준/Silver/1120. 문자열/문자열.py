a, b = input().split(" ")
a = list(a)
b = list(b)
dif = len(b) - len(a)
sum = []
total = 0
for i in range(dif+1):
    for j in range(len(a)):
        if a[j] != b[j+i]:
            total += 1
    sum.append(total)
    total = 0
sum.sort()
print(sum[0])
