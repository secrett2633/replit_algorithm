import sys
import heapq
input = sys.stdin.readline
n = int(input())
cache = {}
for i in range(n):
  s = input().rstrip()
  try:
    cache[s[0]] += 1
  except:
    cache[s[0]] = 1
ans = []
for i in cache:
  if cache[i] >= 5: ans.append(i)
ans.sort()
if ans: print("".join(ans))
else: print("PREDAJA")
    