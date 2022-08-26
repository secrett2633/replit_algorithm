import sys
import heapq
input = sys.stdin.readline
s = ""
for i in range(1, 100001):
    s += str(i)
n = input().rstrip()
print(s.index(n) + 1)