import sys
from collections import Counter
input = sys.stdin.readline
while True:
  s = input().rstrip().lower()
  if s == "#":
    break
  s = Counter(list(s))
  print(s['a'] + s['e'] + s['i'] + s['o'] + s['u'])
  