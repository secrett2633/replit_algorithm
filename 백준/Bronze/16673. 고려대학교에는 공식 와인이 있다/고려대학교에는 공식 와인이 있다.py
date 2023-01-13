a, b, c = map(int, input().split())
res = 0
for i in range(1, a + 1):
    res += b * i + c * (i ** 2)
print(res)