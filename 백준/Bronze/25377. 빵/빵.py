res = 1001
for i in range(int(input())):
  a, b = map(int, input().split())
  if a <= b: res = min(res, b)
if res != 1001: print(res)
else: print(-1)