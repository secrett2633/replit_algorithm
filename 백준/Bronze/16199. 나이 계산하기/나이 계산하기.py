import sys
import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
x1, x2, x3 = map(int, input().rstrip().split())
y1, y2, y3 = map(int, input().rstrip().split())
if x2 < y2 or (x2 == y2 and x3 <= y3):
  print(y1 - x1)
else:
  print(max(y1 - x1 - 1, 0))
print(y1 - x1 + 1)
print(y1 - x1)