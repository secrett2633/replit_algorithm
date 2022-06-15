import sys
input = sys.stdin.readline
res = 0
for i in range(int(input())):
  s = list(input().rstrip())
  cache = set()
  prev = s[0]
  for i in range(len(s)):
    if s[i] != prev and s[i] in cache:
      break
    cache.add(s[i])
    prev = s[i]
    if i == len(s) - 1:
      res += 1
print(res)