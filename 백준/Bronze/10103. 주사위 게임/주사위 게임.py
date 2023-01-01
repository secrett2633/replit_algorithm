import sys
import heapq
input = sys.stdin.readline
c = d = 100
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b: d -= a
    elif a < b: c -= b
print(c)
print(d)