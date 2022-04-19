import sys
input = sys.stdin.readline
for _ in range(int(input())):
  m, n, x, y = map(int, input().split())
  
  while m * n > x:
    if (x - y) % n == 0:
      break
    x += m
  if x >= m * n:
    print("-1")
  else:
    print(x)