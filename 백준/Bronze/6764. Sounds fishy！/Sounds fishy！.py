import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
arr = [int(input()) for _ in range(4)]
if arr[0] < arr[1] < arr[2] < arr[3]:
  print("Fish Rising")
elif arr[0] > arr[1] > arr[2] > arr[3]:
  print("Fish Diving")
elif arr[0] == arr[1] == arr[2] == arr[3]:
  print("Fish At Constant Depth")
else:
  print("No Fish")