import sys
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a, b = map(int, input().split())
c, d = map(int, input().split())
print(min(a + d, b + c))