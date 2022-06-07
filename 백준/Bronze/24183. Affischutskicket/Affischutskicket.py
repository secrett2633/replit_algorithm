import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a, b, c = map(int, input().split())
x = 0.229 * 0.324 * 2
y = 0.297 * 0.420 * 2
z = 0.210 * 0.297
print(a * x + b * y + c * z)
