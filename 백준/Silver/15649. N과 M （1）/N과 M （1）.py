import sys
#from collections import deque
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n, m = map(int, input().split())
def dfs(s):
  if len(s) == m:
    print(*s)
    return
  for i in range(1, n + 1):
    if i not in s:
      dfs(s + [i])
dfs([])