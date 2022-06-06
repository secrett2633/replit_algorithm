import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a, b, c = map(int, input().split())
x, y, z = map(int, input().split())
print(max(x - a, 0) + max(y - b, 0) + max(z - c, 0))