while True:
      q =int(input())
      if q == 0:
            break
      n = q * 2
      a = [False,False] + [True]*(n-1)
      primes=[]

      for i in range(2,n+1):
        if a[i]:
          primes.append(i)
          for j in range(2*i, n+1, i):
              a[j] = False
      cnt = 0
      for i in primes:
            if i > q and i <= 2 * n:
                  cnt += 1
      print(cnt)