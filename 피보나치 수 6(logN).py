import sys
sys.setrecursionlimit(10 ** 9)
n = int(input())
cache = {0 : 0, 1 : 1, 2 : 1}
def solve(now):
  if cache.get(now) != None:
    return cache[now]
  if now % 2 == 1:
    cache[now // 2 + 1] = solve(now // 2 + 1) % 1000000007
    cache[now // 2] = solve(now // 2) % 1000000007
    return cache[now // 2 + 1] ** 2 + cache[now // 2] ** 2
  else:
    cache[now // 2 + 1] = solve(now // 2 + 1) % 1000000007
    cache[now // 2 - 1] = solve(now // 2 - 1) % 1000000007
    return cache[now // 2 + 1] ** 2 - cache[now // 2 - 1] ** 2

print(solve(n) % 1000000007)