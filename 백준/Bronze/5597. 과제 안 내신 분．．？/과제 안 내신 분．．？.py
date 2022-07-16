import sys
arr = list(range(1, 31))
for _ in range(28):
  arr.remove(int(sys.stdin.readline()))
print(arr[0])
print(arr[1])