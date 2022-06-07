import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a, c, e = map(float, input().split())
x, y, z = map(float, input().split())
res = "E"
if z >= e and y >= c and x >= a:
  res = "A"
elif z >= e and y >= c:
  res = "C"
  if x >= a * 0.5:
    res = "B"
elif z >= e:
  if y >= c * 0.5:
    res = "D"
print(res)