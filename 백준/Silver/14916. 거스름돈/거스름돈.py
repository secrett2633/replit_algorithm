import sys
input = sys.stdin.readline
n = int(input())
a = n // 5
res = int(1e9)
while a > -1:
  temp = n - a * 5
  if temp % 2 == 0:
    res = min(temp // 2 + a, res)
  a -= 1
print(res if res != int(1e9) else -1)