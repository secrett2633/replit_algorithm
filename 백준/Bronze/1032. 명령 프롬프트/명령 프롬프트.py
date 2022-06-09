import sys
import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
res = ""
for i in range(len(arr[0])):
  temp = arr[0][i]
  for j in range(1, n):
    if arr[j][i] != temp:
      temp = "?"
      break
  res += temp
print(res)
    