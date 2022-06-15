import sys
input = sys.stdin.readline
def checkPrimeNum(check_number):
    for i in range(2, 1000001): 
        if int(check_number) % i == 0: 
            return False
    return True
n = int(input())
for _ in range(n):
  s = int(input())
  if checkPrimeNum(s):
    print("YES")
  else:
    print("NO")