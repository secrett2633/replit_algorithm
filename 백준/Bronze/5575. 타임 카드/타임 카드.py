import sys
#from collections import Counter
input = sys.stdin.readline
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
x = (a[3] * 3600 + a[4] * 60 + a[5]) - (a[0] * 3600 + a[1] * 60 + a[2])
y = (b[3] * 3600 + b[4] * 60 + b[5]) - (b[0] * 3600 + b[1] * 60 + b[2])
z = (c[3] * 3600 + c[4] * 60 + c[5]) - (c[0] * 3600 + c[1] * 60 + c[2])
x1, x = divmod(x, 3600)
x2, x = divmod(x, 60)
print(x1, x2, x)
x1, y = divmod(y, 3600)
x2, y = divmod(y, 60)
print(x1, x2, y)
x1, z = divmod(z, 3600)
x2, z = divmod(z, 60)
print(x1, x2, z)