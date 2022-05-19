import sys
input = sys.stdin.readline
s = input()
n = 0
arr = ["U", "C", "P", "C"]
for i in s:
  if i == arr[n]:
    n += 1
    if n == 4:
      print("I love UCPC")
      sys.exit()
print("I hate UCPC")