import sys
input = sys.stdin.readline
import math
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(max(sum(a), sum(b)))