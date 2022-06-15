num = int(input())
number = input().split(" ")
for i in range(num):
      number[i] = int(number[i])
number.sort()
total = 1
for i in range(num):
      if total  < number[i]:
            break
      else:
            total += number[i]
print(total)           