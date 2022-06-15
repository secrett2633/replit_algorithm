import sys
sys.setrecursionlimit(1000000)
n, m = input().split()
n = int(n)
m = int(m)
list1 = list(map(int, input().split()))
list1.sort()
def abc(leng, a, b, c, goal, sim):
      if list1[a] + list1[b] + list1[c] == goal:
            return goal
      else:
            if list1[a] + list1[b] + list1[c] > goal:
                  temp = 0
            else:
                  temp = list1[a] + list1[b] + list1[c]
            if c + 1 < leng:
                  return abc(leng, a, b, c + 1, goal, max(temp, sim))
            elif b + 2< leng:
                  return abc(leng, a, b + 1, b + 2, goal, max(temp, sim))
            elif a + 3 < leng:
                  return abc(leng, a + 1, a + 2, a + 3, goal, max(temp, sim))
            else:
                  return max(temp, sim)
print(abc(n, 0, 1, 2, m, 0))