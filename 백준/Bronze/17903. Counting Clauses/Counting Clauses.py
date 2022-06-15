import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
m, n = map(int, input().split())
res = 1
for i in range(m):
  a, b, c = map(int, input().split())
if m >= 8:
  print("satisfactory")
else:
  print("unsatisfactory")