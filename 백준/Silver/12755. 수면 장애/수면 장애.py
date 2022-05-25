import sys
input = sys.stdin.readline
n = int(input())
res = ""
now = 1
while len(str(now)) < n:
  res = str(now)
  n -= len(str(now))
  now += 1
res = str(now)
print(res[n - 1])