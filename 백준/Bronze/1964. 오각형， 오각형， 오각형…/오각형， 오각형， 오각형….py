n = int(input())
res = 5
for i in range(2, n + 1):
    res += (i * 3 + 1)
print(res % 45678)