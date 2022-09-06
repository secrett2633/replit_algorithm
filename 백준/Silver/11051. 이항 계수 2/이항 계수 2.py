import sys
import math
input = sys.stdin.readline
n, k = list(map(int, input().split()))
res = 1
for i in range(k):
    res *= (n - i)
for i in range(1, k + 1):
    res //= i
print(res % 10007)