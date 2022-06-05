import sys
#from math import sqrt
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n, m, k = map(int, input().rstrip().split())
print(min(k, m) + min(n - k, n - m))