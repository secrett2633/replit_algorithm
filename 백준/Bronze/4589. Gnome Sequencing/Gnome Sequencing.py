n = int(input())
print("Gnomes:")
for _ in range(n):
  arr = list(map(int, input().split()))
  if arr == sorted(arr) or arr[::-1] == sorted(arr): print("Ordered")
  else: print("Unordered")