import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n = int(input())

if n == 1 or n == 0:
  print(1)
elif n == 2:
  print(2)
elif n == 3:
  print(6)
elif n == 4:
  print(4)
else:
  print(0)