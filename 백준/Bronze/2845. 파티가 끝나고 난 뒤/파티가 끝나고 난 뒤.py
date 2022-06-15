import sys
import math
input = sys.stdin.readline
l, p = map(int, input().split())
par = list(map(int, input().split()))
for i in range(len(par)): par[i] -= (l * p)
print(" ".join(map(str, par)))