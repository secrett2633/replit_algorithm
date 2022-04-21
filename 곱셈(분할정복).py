import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())
def solve(num, n):
  if n == 1:
    return num % c
  result = solve(num, n // 2)
  if n % 2 == 1:
    return result * result * num % c
  else:
    return result * result % c
print(solve(a, b) % c)