import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = []
for i in range(n):
  temp = set()
  for j in range(5):
    for k in range(n):
      if arr[k][j] == arr[i][j] and k != i:
        temp.add(k)
  res.append(len(temp))
print(res.index(max(res)) + 1)