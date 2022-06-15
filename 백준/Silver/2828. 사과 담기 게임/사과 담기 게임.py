n, m = map(int, input().split())
apple = int(input())
location = [int(input()) for _ in range(apple)]
basket = [1, m]
move = 0
for i in range(apple):
      if location[i] > basket[1]:
            temp = location[i] - basket[1]
            basket[1] += temp
            basket[0] += temp
            move += temp
      elif location[i] < basket[0]:
            temp = basket[0] - location[i]
            basket[1] -= temp
            basket[0] -= temp
            move += temp
      else:
            continue
print(move)