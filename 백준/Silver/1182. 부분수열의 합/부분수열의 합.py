import sys
#sys.setrecursionlimit(10 ** 6)
from itertools import combinations
#from collections import deque
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
n, s = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
for i in range(1, n + 1):
  for j in combinations(arr, i):
    if sum(j) == s:
      res += 1
print(res)