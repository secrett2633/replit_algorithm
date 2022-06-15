import sys
import math
input = sys.stdin.readline
n = int(input())
arr = sorted([int(input()) for _ in range(n)])

def get_divisor(num):
    divisors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num//i)
    divisors.sort()
    return divisors
  
for i in range(1, n):
  res = get_divisor(arr[i] - arr[i - 1])
  if i == 1:
    result = res
  else:
    result = list(set(res) & set(result))
print(" ".join(map(str, result[1:])))