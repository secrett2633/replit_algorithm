import sys
from itertools import product
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
s = input().rstrip()
res = [0] * 53
for i in arr:
  res[i] += 1
visited = [0] * 53
for i in s:
  if i == " ": visited[0] += 1
  elif i.isupper(): visited[ord(i) - 64] += 1
  else: visited[ord(i) - 70] += 1
if res == visited: print("y")
else: print("n")
  