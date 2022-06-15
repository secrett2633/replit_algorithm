import math
n = int(input())
student = input().split(" ")
b, c = input().split(" ")
b = int(b)
c = int(c)
temp = []
sum = n
for i in range(n):
      student[i] = int(student[i])
      temp.append(student[i] - b)
for i in temp:
      if i > 0:
            sum +=math.ceil(i / c)
print(sum)