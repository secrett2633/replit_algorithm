import sys
input = sys.stdin.readline
a, b = input().rstrip().split()
c = a.index(".")
a, c = int(a[:c] + a[c + 1:]) ** int(b), (10 ** (len(a) - c - 1)) ** int(b)
if len(str(a)) - len(str(c)) + 1 >= 0: print(f"{str(a)[:len(str(a)) - len(str(c)) + 1]}.{str(a)[len(str(a)) - len(str(c)) + 1:]}")
else: print("0." + "0" * -(len(str(a)) - len(str(c)) + 1) + str(a))