import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if 8 <= a <= 9 and 8 <= d <= 9 and b == c:
  print("ignore")
else:
  print("answer")