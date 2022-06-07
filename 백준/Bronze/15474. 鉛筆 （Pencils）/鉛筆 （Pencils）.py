import sys
import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n, a, b, c, d = map(int, input().split())
print(min(math.ceil(n / a) * b, math.ceil(n / c) * d))