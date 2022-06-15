n = int(input())
dow, topping = input().split()
dow = int(dow)
topping = int(topping)
dow_price = int(input())
topping_price = [int(input()) for i in range(n)]
topping_price.sort(reverse = True)
result = [dow_price, dow]
for i in range(n):
      if result[0] / result[1] < topping_price[i] / topping:
            result[0] += topping_price[i]
            result[1] += topping
print(result[0] // result[1])