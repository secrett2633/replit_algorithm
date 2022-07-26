import sys
input = sys.stdin.readline
n = int(input())
s = input().rstrip()
cnt = 0
for _ in range(n):
  t = input().rstrip()
  flag = False
  for i in range(34):
    if flag or (len(s) - 1) * i + len(s) > len(t): break
    for j in range(len(t)):
      for k in range(len(s)):
        if j + i * k + k >= len(t): break
        if s[k] != t[j + i * k + k]: break
      else: flag = True
  if flag: cnt += 1  
print(cnt)