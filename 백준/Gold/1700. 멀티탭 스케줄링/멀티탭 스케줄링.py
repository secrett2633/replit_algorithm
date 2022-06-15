n, k = input().split()
n = int(n)
k = int(k)
list1 = list(map(int, input().split()))
def future(target, small_list):
      i = 0
      while i < len(small_list):
            if small_list[i] == target:
                  return i
            else:
                  i += 1
      return 10000
multi_tap = []
cnt = 0
for i in range(k):
      if list1[i] in multi_tap:
            continue
      elif len(multi_tap) < n:
            multi_tap.append(list1[i])
      else:
            temp = -1
            temp2 = [0]
            for target in multi_tap:
                  temp1 = future(target, list1[i:])
                  if temp1 == -1:
                        temp2[0] = target
                        break
                  elif temp1 > temp:
                        temp = temp1
                        temp2[0] = target
            multi_tap.remove(temp2[0])
            multi_tap.append(list1[i])
            cnt += 1
print(cnt)