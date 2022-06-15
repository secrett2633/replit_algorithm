import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())
res = a + max(0, t - 30) * x * 21
res1 = b + max(0, t - 45) * y * 21
print(res, res1)