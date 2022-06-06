import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = max(max(a[2], b[2]) - min(a[0], b[0]), max(a[3], b[3]) - min(a[1], b[1]))
print(x * x)