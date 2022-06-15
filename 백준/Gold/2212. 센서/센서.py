n = int(input())
k = int(input())
location = list(map(int, input().split()))
location.sort()
dis = []
for i in range(1, len(location)):
      dis.append(location[i] - location[i - 1])
dis.sort(reverse = True)
answer = location[-1] - location[0]
if k > n:
      k = n
for i in range(k - 1):
      answer -= dis[i]
print(answer)