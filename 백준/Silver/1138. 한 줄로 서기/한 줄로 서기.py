n = int(input())
line = []
people = [-1] + list(map(int, input().split()))
for i in range(n, 0, -1):
      line.insert(people[i], i)
print(*line)