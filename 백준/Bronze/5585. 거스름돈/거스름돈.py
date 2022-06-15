m = 1000 - int(input())
n = 0
count_list = [500, 100, 50, 10, 5, 1]
for i in count_list:
    n += m//i
    m -= m//i * i    
print(n)
