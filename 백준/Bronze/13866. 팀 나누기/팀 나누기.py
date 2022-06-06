import sys
import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a, b, c, d = map(int, input().rstrip().split())
x = a + b - c - d
y = a + c - b - d
z = a + d - b - c
print(min(abs(x), abs(y), abs(z)))