def first(num):
      if num < 1:
            return 0
      elif num <= 1:
            return 5000000
      elif num <= 3:
            return 3000000
      elif num <= 6:
            return 2000000
      elif num <= 10:
            return 500000
      elif num <= 15:
            return 300000
      elif num <= 21:
            return 100000
      else:
            return 0
def second(num):
      if num < 1:
            return 0
      elif num <= 1:
            return 5120000
      elif num <= 3:
            return 2560000
      elif num <= 7:
            return 1280000
      elif num <= 15:
            return 640000
      elif num <= 31:
            return 320000
      else:
            return 0
for i in range(int(input())):
      a, b = input().split(" ")
      print(first(int(a)) + second(int(b)))