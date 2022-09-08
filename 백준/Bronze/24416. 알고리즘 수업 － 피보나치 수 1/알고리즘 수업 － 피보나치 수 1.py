import sys
import math
input = sys.stdin.readline
n = int(input())
res = [0]
def fib(now):
    if now == 1 or now == 2: 
        res[0] += 1
        return 1
    else: 
        return (fib(now - 1) + fib(now - 2))
fib(n)
print(res[0], n - 2)