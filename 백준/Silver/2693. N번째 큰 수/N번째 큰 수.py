import sys
input = sys.stdin.readline
for _ in range(int(input())):
  arr = sorted(list(map(int, input().split())))
  print(arr[7])