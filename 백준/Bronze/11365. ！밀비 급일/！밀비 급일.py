import sys
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
while True:
  s = input().rstrip()
  if s == "END":
    break
  print(s[::-1])