import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())
print(min(a * p, b + max(p - c, 0) * d))
