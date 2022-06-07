import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a, b, c = map(int, input().split())
if a + b + c <= 4:
  print(1)
else:
  print(2)