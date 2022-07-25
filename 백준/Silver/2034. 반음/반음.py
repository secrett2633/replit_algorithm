import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
cache = ["A", "*", "B", "C", "*", "D", "*", "E", "F", "*", "G", "*"]
res = []
for start in [0, 2, 3, 5, 7, 8, 10]:
  tmp = start
  for i in arr:
    start = (start + 24 + i) % 12
    if cache[start] == "*": break
  else:
    res.append([cache[tmp], cache[start]])
for i in res:
  print(*i)