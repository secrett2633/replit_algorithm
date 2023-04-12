import sys
#from collections import deque
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))
min_res = int(1e9)
max_res = -int(1e9)
def solve(now, cnt, a, b, c, d):
  if cnt == n:
    global min_res
    global max_res
    min_res = min(min_res, now)
    max_res = max(max_res, now)
    return
  if a > 0:
    solve(now + arr[cnt], cnt + 1, a - 1, b, c, d)
  if b > 0:
    solve(now - arr[cnt], cnt + 1, a, b - 1, c, d)
  if c > 0:
    solve(now * arr[cnt], cnt + 1, a, b, c - 1, d)
  if d > 0:
    solve(int(now / arr[cnt]), cnt + 1, a, b, c, d - 1)
solve(arr[0], 1, op[0], op[1], op[2], op[3])
print(max_res)
print(min_res)