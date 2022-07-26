import sys
input = sys.stdin.readline
while True:
  try:
    s, t = input().rstrip().split()
  except:
    break
  n = 0
  flag = False
  for i in range(len(t)):
    if s[n] == t[i]: n += 1
    if n == len(s): flag = True; break
  if flag: print("Yes")
  else: print("No")