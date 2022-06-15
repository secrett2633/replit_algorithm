n, k = input().split(" ")
n = int(n)
k = int(k)
price = []
sum = 0
for i in range(n):
    price.append(int(input()))
price.reverse()
for i in price:
    sum += k//i
    k = k%i
print(sum)
