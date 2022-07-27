import sys
input = sys.stdin.readline
for _ in range(int(input())):
  a, b = map(int, input().split())
  a = int(str(a)[-1])
  res = a
  for i in range(b - 1):
    res *= a
    res = int(str(res)[-1])
  print(res if res != 0 else 10)