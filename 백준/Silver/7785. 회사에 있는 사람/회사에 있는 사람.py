import sys
input = sys.stdin.readline
name = set()
for _ in range(int(input())):
  a, b = input().rstrip().split()
  if b == "enter":
    name.add(a)
  else:
    name.remove(a)
name = list(name)
name.sort(reverse = True)
print("\n".join(name))