import sys
input = sys.stdin.readline
D, P, Q = map(int, input().split())
if D % P == 0 or D % Q == 0: 
  print(D)
  exit(0)
P, Q = max(P, Q), min(P, Q)
n = D // P + 1
answer = P * n

for i in range(n - 1, -1, -1):
    div, mod = divmod((D - (i * P)), Q) 
    if mod == 0: 
      print(D)
      exit(0)
    temp = (div + 1) * Q + i * P 
    if answer == temp: 
      break 
    answer = min(answer, temp)
print(answer)