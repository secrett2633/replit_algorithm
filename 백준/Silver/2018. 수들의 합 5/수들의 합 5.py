import sys
#from itertools import combinations
#from collections import Counter
input = sys.stdin.readline
n = int(input())
left = 1
right = 1
now = 1
res = 0
while(left <= right):
    if now == n:
        res += 1
    if now < n:
        right += 1
        now += right
    elif now >= n:
        now -= left
        left += 1
print(res)