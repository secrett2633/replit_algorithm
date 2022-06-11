import sys
#from collections import deque
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(range(1, n + 1))
now = 0
res = []
for t in range(n):
  now += k - 1  
  if now >= len(arr):
    now = now % len(arr)
  res.append(str(arr.pop(now)))
print("<",", ".join(res),">", sep='')