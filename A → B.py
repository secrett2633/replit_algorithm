import sys
sys.setrecursionlimit(10**9)
a, b = map(int, input().split())
cache = dict()
def solve(now, cnt):
  if now in cache:
    if cache[now] <= cnt:
      return
  cache[now] = cnt
  if now >= b:
    return  
  solve(now * 2, cnt + 1)
  solve(now * 10 + 1, cnt + 1)

solve(a, 0)
print(cache[b] + 1 if b in cache else "-1")
