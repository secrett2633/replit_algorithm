import sys
input = sys.stdin.readline
while True:
  n = int(input())
  if n == 0: break
  s = input().split(",")
  res = set()
  for i in s:
    if "-" in i:
      a, b = i.split("-")
      for j in range(int(a), int(b) + 1):
        if j <= n: res.add(j)
    else:
      if int(i) <= n: res.add(int(i))
  print(len(res))