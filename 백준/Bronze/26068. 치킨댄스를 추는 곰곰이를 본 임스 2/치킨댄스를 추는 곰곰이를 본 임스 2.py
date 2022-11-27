n = int(input())
res = 0
for _ in range(n):
    a = int(input().rstrip()[2:])
    if a <= 90: res += 1
print(res)