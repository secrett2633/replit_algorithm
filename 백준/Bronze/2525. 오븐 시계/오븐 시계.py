import sys
input = sys.stdin.readline
a, b = map(int, input().split())
c = int(input())
res = a * 60 + b + c
a, b = divmod(res, 60)
print(a % 24, b)