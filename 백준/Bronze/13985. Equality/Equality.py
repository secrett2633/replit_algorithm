import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
s = list(input().rstrip().split())
if int(s[0]) + int(s[2]) == int(s[4]):
  print("YES")
else:
  print("NO")