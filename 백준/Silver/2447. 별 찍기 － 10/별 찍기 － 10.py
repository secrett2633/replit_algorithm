import sys
sys.setrecursionlimit(10 ** 6)
#from collections import deque
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n = int(input())
def solve(cnt):
  if cnt == 1:
    return ['*']
  temp = solve(cnt // 3) 
  res = []      
  for i in temp:
    res.append(i * 3)
  for i in temp:
    res.append(i + ' ' * (cnt // 3) + i)
  for i in temp:
    res.append(i * 3)
  return res
print('\n'.join(solve(n)))