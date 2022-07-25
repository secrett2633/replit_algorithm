x, y = map(int, input().split())
res = 1000 / y * x
for _ in range(int(input())):
  x, y = map(int, input().split())
  res = min(res, 1000 / y * x)
print(round(res, 2))