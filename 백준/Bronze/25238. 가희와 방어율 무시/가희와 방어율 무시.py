import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a, b = map(int, input().split())
res = a - a * (b / 100)
if res >= 100:
  print("0")
else:
  print(1)