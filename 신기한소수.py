import math
a = int(input())
n = 10 ** a # 2부터 1,000까지의 모든 수에 대하여 소수 판별

def aratos(n):
  array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화
  for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
      if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
          # i를 제외한 i의 모든 배수를 지우기
          j = 2 
          while i * j <= n:
              array[i * j] = False
              j += 1
  return array[n]
          
start = 10 ** (a - 1)
while start < n:
  cnt = 0
  temp = str(start)
  for i in range(1, a + 1):
    if aratos(int(temp[:i])) and int(temp[:i]) != 1:
      cnt += 1
  if cnt == a:
    print(str(start))
  start += 1

