import sys
from collections import deque
from string import ascii_lowercase
alphabet_list = ascii_lowercase
input = sys.stdin.readline
n = int(input())
temp = list(input())
cnt = 0
for i in range(n):
  cnt += ((alphabet_list.find(temp[i]) + 1) * (31 ** i)) % 1234567891

print(cnt % 1234567891)