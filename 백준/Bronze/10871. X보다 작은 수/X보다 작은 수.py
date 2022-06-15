n, x = input().split()
n = int(n)
x = int(x)
string = input().split()
for i in range(n):
      if int(string[i]) < x:
            print("%s " % (string[i]), end = "")
print("")