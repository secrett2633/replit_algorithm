import sys
import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
t1, m1, t2, m2 = map(int, input().split())
a = t1 * 60 + m1
b = t2 * 60 + m2
m = (b - a)
if m < 0: m += 1440
n = m // 30
print(m, n)