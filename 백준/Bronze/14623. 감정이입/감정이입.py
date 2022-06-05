import sys
from math import sqrt
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a = int(input(), 2)
b = int(input(), 2)
print(bin(a * b)[2:])