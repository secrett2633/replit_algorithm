import sys
input = sys.stdin.readline
n = int(input())
def return_sum(num):
  num1 = str(num)
  cnt = num
  for i in range(len(num1)):
    cnt += int(num1[i])
  return cnt
  
for i in range(n):
  if return_sum(i) == n:
    print(i)
    break
  if i == n - 1:
    print("0")
  