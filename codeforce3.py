import sys
from collections import Counter
input = sys.stdin.readline
t = int(input())
for i in range(t):
  n = int(input())
  arr = list(map(int, input().split()))
  cnt = True
  cnt1 = True
  for i in arr:
    if i % 2 == 1:
      cnt = False
    else:
      cnt1 = False
  if cnt or cnt1:
    print("YES")
    continue
    
  cnt = True
  cnt1 = True
  for i in range(0, n, 2):
    if arr[i] % 2 == 1:
      cnt = False
    else:
      cnt1 = False
  cnt2 = True
  cnt3 = True
  for i in range(1, n, 2):
    if arr[i] % 2 == 1:
      cnt2 = False
    else:
      cnt3 = False
  if (cnt or cnt1) and (cnt2 or cnt3):
    print("YES")
    continue
  else:
    print("NO")
    
    
    
  
  