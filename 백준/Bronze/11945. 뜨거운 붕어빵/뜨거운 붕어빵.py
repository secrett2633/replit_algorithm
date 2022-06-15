import sys
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n, m = map(int, input().split())
for i in range(n):
  s = input().rstrip()
  print(s[::-1])