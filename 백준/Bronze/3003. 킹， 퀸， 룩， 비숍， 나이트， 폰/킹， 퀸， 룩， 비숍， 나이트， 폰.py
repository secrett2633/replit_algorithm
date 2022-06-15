import sys
import math
input = sys.stdin.readline
par = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]
for i in range(len(par)): par[i] = chess[i] - par[i]
print(" ".join(map(str, par)))