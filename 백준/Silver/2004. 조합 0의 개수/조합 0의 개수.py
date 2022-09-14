import copy
import sys
import heapq
from collections import Counter
input = sys.stdin.readline
n, m = map(int, input().split())
def s(num):
    i = 2
    a, b = 0, 0
    while num >= i:
        a += (num // i)
        i *= 2
    i = 5
    while num >= i:
        b += (num // i)
        i *= 5
    return a, b
            
res = [0, 0]
a, b = s(n)
res[0] += a
res[1] += b
a, b = s(n - m)
res[0] -= a
res[1] -= b
a, b = s(m)
res[0] -= a
res[1] -= b
print(max(min(res), 0))           