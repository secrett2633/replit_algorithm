import sys
input = sys.stdin.readline
n, b, h, w = map(int, input().split())
res = int(1e9)
for _ in range(h):
  p = int(input())
  arr = list(map(int, input().split()))
  if max(arr) > w: res = min(res, n * p)
if res > b: print("stay home")
else: print(res)