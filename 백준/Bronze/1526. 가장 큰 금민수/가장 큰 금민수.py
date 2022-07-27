import sys
input = sys.stdin.readline
n = input().rstrip()
ans = ""
a = 0
for i in n:
  a = a * 10 + int(i)
  if a >= 7: ans += "7"; a -= 7
  elif a >= 4: ans += "4"; a -= 4
  else: ans += "0"
for i in range(int(ans), 0, -1):
  for j in str(i):
    if j != "7" and j != "4": break
  else: print(i); break