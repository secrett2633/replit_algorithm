import sys
input = sys.stdin.readline
while True:
  a, b = map(int, input().split())
  x, y = a, b
  if a == 0 and b == 0: break
  visited1 = [a]
  visited2 = [b]
  while True:
    tmp = 0
    for i in str(visited1[-1]):
      tmp += int(i) ** 2
    if tmp in visited1: break
    else: visited1.append(tmp)
  while True:
    tmp = 0
    for i in str(visited2[-1]):
      tmp += int(i) ** 2
    if tmp in visited2: break
    else: visited2.append(tmp)
  flag = False
  res = 0
  for i in visited1:
    if i in visited2: res = visited1.index(i) + 2 + visited2.index(i); break
  for i in visited2:
    if i in visited1: 
      if res > visited2.index(i) + 2 + visited1.index(i): res = visited2.index(i) + 2 + visited1.index(i); break
  print(x, y, res)
  