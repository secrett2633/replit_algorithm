import sys
import copy
import heapq
from itertools import combinations
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())    
    if n == 1: print(1)
    else:
      x = 2
      n -= 2
      ans = 1
      while n:
        if n & 1:
          ans *= x
          ans %= 1000000007
        n //= 2
        x *= x
        x %= 1000000007
      print(ans)