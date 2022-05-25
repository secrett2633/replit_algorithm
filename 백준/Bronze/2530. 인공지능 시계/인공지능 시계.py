import sys
input = sys.stdin.readline
import math
a, b, c = map(int, input().split())
d = int(input())
res = a * 3600 + b * 60 + c + d
a, res = divmod(res, 3600)
b, res = divmod(res, 60)
print(a % 24, b % 60, res)
