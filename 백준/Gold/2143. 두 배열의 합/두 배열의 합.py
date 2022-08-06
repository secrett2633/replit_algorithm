import sys
import copy
import heapq
import bisect
from itertools import combinations
input = sys.stdin.readline
t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
sa = []
sb = []
for i in range(n):
  sa.append(a[i])
  for j in range(i + 1, n):
    sa.append(sa[-1] + a[j])
for i in range(m):
  sb.append(b[i])
  for j in range(i + 1, m):
    sb.append(sb[-1] + b[j])
sa.sort()
sb.sort()
answer = 0
for i in sa:
  answer += bisect.bisect_right(sb, t - i) - bisect.bisect_left(sb, t - i)
print(answer)