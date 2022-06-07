import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
x1, x2, y1, y2 = map(int, input().split())
res = (x1 * y1) / (x2 * y2) / 2
if res == int(res):
  print(1)
else:
  print(0)