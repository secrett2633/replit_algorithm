import sys
#from collections import Counter
input = sys.stdin.readline
a = int(input())
b = int(input())
if b - a <= 0:
  print("Congratulations, you are within the speed limit!")
elif 1 <= b - a <= 20:
  print("You are speeding and your fine is $100.")
elif 21 <= b - a <= 30:
  print("You are speeding and your fine is $270.")
else:
  print("You are speeding and your fine is $500.")