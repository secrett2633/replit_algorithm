import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a, b = map(int, input().split())
x = (a - (a // 2) * 2) * b
y = (b - (b // 2) * 2) * a
print(min(x, y))