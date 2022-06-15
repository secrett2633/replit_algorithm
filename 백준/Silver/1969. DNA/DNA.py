n, m = input().split(" ")
n = int(n)
m = int(m)
dna = []
for i in range(n):
      dna.append(input())

temp = []
final = []
temp1 = []
count = 0
final1 = []
for i in range(m):
      temp = []
      temp1 = []
      final1 = []
      for t in range(n):
            temp1.append(dna[t][i])
      for j in range(n):
            temp.append(temp1.count(temp1[j]))
      for k in range(n):
            if temp[k] == max(temp) and len(final) == i:                  
                  final1.append(dna[k][i])
      final1.sort()
      final.append(final1[0])
      for d in range(n):
            if dna[d][i] != final[i]:
                  count += 1
print(''.join(final))
print(count)           