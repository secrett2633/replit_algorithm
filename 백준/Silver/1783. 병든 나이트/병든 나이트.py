a, b = input().split(" ")
a = int(a)
b = int(b)
if a == 1:
      print("1")
elif a ==2 :
      print(min(4, int((b+1)/2)))
else:
      if b < 7:
            print(min(b, 4))
      else:
            print(b-2)
