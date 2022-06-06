import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n = int(input()) % 8
if n == 1:
  print(1)
elif n == 2 or n == 0:
  print(2)
elif n == 3 or n == 7:
  print(3)
elif n == 4 or n == 6:
  print(4)
else:
  print(5)