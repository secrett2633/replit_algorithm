import sys
from collections import Counter
input = sys.stdin.readline
t = int(input())
for i in range(t):
  n = int(input())
  arr = Counter(list(map(int, input().split())))
  arr_set = list(set(arr))
  cnt = True
  for i in arr_set:
    if arr[i] >= 3:
      print(i)
      cnt = False
      break
  if cnt:
    print("-1")
    
    
  
  