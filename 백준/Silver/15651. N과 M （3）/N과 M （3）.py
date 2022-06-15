import sys
sys.setrecursionlimit(10 ** 6)
#from collections import deque
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n, m = map(int, input().split())
def solve(now, cnt):
  if cnt == m:
    print(*now)
    return
  for i in range(1, n + 1):
    solve(now + [i], cnt + 1)
solve([], 0)