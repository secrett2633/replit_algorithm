while True:
      n, a, b = input().split()
      n = int(n)
      a = int(a)
      b = int(b)
      answer = 0
      if n == 0 and a == 0 and b == 0:
            break
      distance = [list(map(int, input().split())) for i in range(n)]
      temp = [[distance[i][2] - distance[i][1], i, distance[i][0]] for i in range(n)]
      i = 0   
      temp.sort(reverse = True)
      while temp[i][0] > 0 and i < n:            
            if temp[i][2] <= a:
                  answer += (temp[i][2] * distance[temp[i][1]][1])
                  a -= temp[i][2]
            else:                  
                  if a > 0:
                        temp1 = temp[i][2] - a
                        answer += (a * distance[temp[i][1]][1]) + (temp1 * distance[temp[i][1]][2])
                        a = 0
                        b -= temp1
                  else:
                        answer += temp[i][2] * distance[temp[i][1]][2]
                        b -= temp[i][2]
            i += 1
            if i >= n:
                  break
      i = n - 1
      while temp[i][0] < 0 and i < n:
            if temp[i][2] <= b:
                  answer += (temp[i][2] * distance[temp[i][1]][2])
                  b -= temp[i][2]
            else:
                  if a > 0:
                        temp1 = temp[i][2] - b
                        answer += (b * distance[temp[i][1]][2]) + (temp1 * distance[temp[i][1]][1])
                        b = 0
                  else:
                        answer += temp[i][2] * distance[temp[i][1]][1]
                        a -= temp[i][2]
            i -= 1
            if i < 0:
                  break
      if i >= 0 and i < n:
            while temp[i][0] ==0 and i < n:
                  answer += (temp[i][2] * distance[temp[i][1]][1])
                  i -= 1
                  if i < 0 or i >= n:
                        break
      print(answer)