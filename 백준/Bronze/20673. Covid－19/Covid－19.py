import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
p = int(input())
q = int(input())
if p <= 50 and q <= 10:
  print("White")
elif q > 30:
  print("Red")
else:
  print("Yellow")