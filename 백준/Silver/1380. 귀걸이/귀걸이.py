import sys
input = sys.stdin.readline
res = 0
while True:
  name = []
  n = int(input())
  if n == 0:
    break
  for _ in range(n):
    name.append(input().rstrip())
  cache = [0] * (n + 1)
  for i in range(2 * n - 1):
    a, b = input().rstrip().split()
    cache[int(a)] += 1
  for i in range(1, n + 1):
    if cache[i] != 2:
      res += 1
      print(res, name[i - 1])
  