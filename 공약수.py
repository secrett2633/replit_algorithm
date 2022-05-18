import sys
import math
input = sys.stdin.readline
def getMyDivisor(n):
    divisorsList = []
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if i ** 2 != n: 
                divisorsList.append(n // i)
    divisorsList.sort()    
    return divisorsList
  
a, b = map(int, input().split())
divisor = getMyDivisor(a * b)
result = []
for i in divisor:
  if a * b // i in divisor:
    if math.gcd(i, a * b // i) == a:
      result.append(((i + a * b // i), i, a * b // i))
result.sort()
print(result[0][1], result[0][2])