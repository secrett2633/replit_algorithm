import sys
input = sys.stdin.readline
n = int(input())
p = res = int(input())
if n >= 20: res = min(res, p * 0.75)
if n >= 15: res = min(res, p - 2000)
if n >= 10: res = min(res, p * 0.9)
if n >= 5: res = min(res, p - 500)
print(max(0, int(res)))