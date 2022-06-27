import sys
#import math
input = sys.stdin.readline
#from itertools import combinations
s = input().rstrip()
n = len(s)
res = []
for i in range(1, n - 1):
  for j in range(1, n - i):
    k = n - i - j
    a, b, c = s[:i], s[i:i+j], s[i+j:]
    res.append(a[::-1] + b[::-1] + c[::-1])
res.sort()
print(res[0])