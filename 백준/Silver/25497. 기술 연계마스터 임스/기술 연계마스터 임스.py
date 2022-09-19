import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
s = input().rstrip()
a = 0
b = 0
res = 0
for i in s:
    if i.isdigit(): res += 1    
    elif i == "R" and a >= 1: res += 1; a -= 1
    elif i == "K" and b >= 1: res += 1; b -= 1
    elif i == "R" or i == "K": break
    elif i == "L": a += 1
    elif i == "S": b += 1
print(res)
