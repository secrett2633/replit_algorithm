import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
  a = int(input())
  if a >= 1900:
    print("Division 1")
  elif a >=1600:
    print("Division 2")
  elif a >=1400:
    print("Division 3")
  else:
    print("Division 4")