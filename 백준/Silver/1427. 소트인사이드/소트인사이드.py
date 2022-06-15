import sys
input = sys.stdin.readline
n = input().rstrip()
n = sorted(n, key = n.find)
n.sort(reverse = True)
print("".join(map(str, n)))