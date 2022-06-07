import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a, b, c = map(int, input().split(" : "))
x, y, z = map(int, input().split(" : "))
res = a * 3600 + b * 60 + c
res1 = x * 3600 + y * 60 + z
print(res1 - res if res1 - res >= 0 else res1 - res + 86400)