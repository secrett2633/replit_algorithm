grade = 0
for i in range(5):
      temp = int(input())
      if temp < 40:
            temp = 40
      grade += temp
print(grade // 5)