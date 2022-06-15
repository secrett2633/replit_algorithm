import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
x = n
y = m
for i in range(n):
  s = list(input().rstrip())
  temp = False
  if "X" in s:
    x -= 1
  arr.append(s)
for i in range(m):
  for j in range(n):
    if arr[j][i] == "X":
      y -= 1
      break
print(max(x, y))     