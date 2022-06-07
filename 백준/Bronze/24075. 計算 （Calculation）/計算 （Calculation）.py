import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a, b = map(int, input().split())
print(max(a + b, a - b))
print(min(a + b, a - b))