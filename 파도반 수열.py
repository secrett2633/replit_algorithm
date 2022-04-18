import sys
t = int(input())
for _ in range(t):
  n = int(input())
  cache = {0 : 1, 1 : 1, 2 : 1}
  for i in range(3, n + 1):
    cache[i] = cache[i - 2] + cache[i - 3]
  print(cache[n - 1])