num, leng = input().split(" ")
num = int(num)
leng = int(leng)
place = input().split(" ")
for i in range(num):
      place[i] = int(place[i])
place.sort()
count = 0
now = 0
for i in range(num):
      if now > place[num-1]:
            break;
      elif now < place[i]+0.49:
            now = place[i] + leng - 0.5
            count += 1
            
print(count)
            
