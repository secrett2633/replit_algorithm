import sys
#from collections import Counter
input = sys.stdin.readline
a, b, c = map(int, input().split())
y = 24 * 60 * a + 60 * b + c
x = 16511
print(y - x if y - x >= 0 else -1)