import sys
#from itertools import combinations
#from collections import Counter
input = sys.stdin.readline
n, k = map(int, input().split())
if k * (k + 1) // 2 > n:
  print("-1")
elif (n - (k + 1) * k // 2) % k == 0:
  print(k - 1)
else:
  print(k)