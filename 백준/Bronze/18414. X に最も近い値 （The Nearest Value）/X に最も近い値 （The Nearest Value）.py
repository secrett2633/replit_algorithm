import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a, b, c = map(int, input().split())
if b <= a <= c:
  print(a)
elif a > c:
  print(c)
else:
  print(b)