import math
m, n, k = input().split(" ")
m = int(m)
n = int(n)
k = int(k)
if m > 2 * n:
    remainder = m - 2 * n
    m = 2 * n
        
elif m < 2 * n:
    remainder = n - math.ceil(m / 2)
    n = math.ceil(m / 2)
else:
    remainder = 0
while True:
    if k > remainder:
        remainder += 2
        n -= 1
        m -= 1
    else:
        break
print((m+n)//3)
