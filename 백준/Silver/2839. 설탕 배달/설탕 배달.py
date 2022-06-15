n = int(input())
five = n // 5
three = 0
start = five * 5
while True:
      if five >= 0:
            now = five * 5 + three * 3
            if (n - now) % 3 == 0:
                  three += (n - now) // 3
                  start == n
                  print(five + three)
                  break
            five -= 1
      else:
            print("-1")
            break