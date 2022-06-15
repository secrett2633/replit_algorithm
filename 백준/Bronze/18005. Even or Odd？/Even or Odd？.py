import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a = int(input()) % 4
if a == 1 or a == 3:
  print(0)
elif a == 2:
  print(1)
else:
  print(2)