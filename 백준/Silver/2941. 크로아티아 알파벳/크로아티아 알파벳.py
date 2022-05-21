import sys
input = sys.stdin.readline
s = list(input().rstrip())
cnt = 0
while s:
  a = s.pop(0)
  if a == "c":
    if len(s) > 0:
      if s[0] == "=" or s[0] == "-":
        s.pop(0)
  elif a == "d":
    try:
      if s[0] == "-":
        s.pop(0)
      elif s[0] == "z" and s[1] == "=":
        s.pop(0)
        s.pop(0)
    except:
      pass
  elif a == "l":
    if len(s) > 0:
      if s[0] == "j":
        s.pop(0)
  elif a == "n":
    if len(s) > 0:
      if s[0] == "j":
        s.pop(0)
  elif a == "s":
    if len(s) > 0:
      if s[0] == "=":
        s.pop(0)
  elif a == "z":
    if len(s) > 0:
      if s[0] == "=":
        s.pop(0)
  cnt += 1
print(cnt)