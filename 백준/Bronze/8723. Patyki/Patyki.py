import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
arr = sorted(list(map(int, input().split())))
if arr[0] * arr[0] + arr[1] * arr[1] == arr[2] * arr[2]:
  print(1)
elif arr[0] == arr[1] == arr[2]:
  print(2)
else:
  print(0)
  
