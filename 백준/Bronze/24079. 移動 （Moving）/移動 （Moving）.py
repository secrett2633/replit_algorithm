import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
x = int(input())
y = int(input())
z = int(input())
if x + y <= z:
  print(1)
else:
  print(0)