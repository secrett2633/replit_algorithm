num = [int(input()) for i in range(3)]
result = str(num[0] * num[1] * num[2])
for i in range(10):
      print(result.count(str(i)))