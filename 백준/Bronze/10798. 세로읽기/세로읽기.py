list1 = [list(input()) for i in range(5)]
answer = []
for i in range(15):
      if list1[0] != []:
            answer.append(list1[0].pop(0))
      if list1[1] != []:
            answer.append(list1[1].pop(0))
      if list1[2] != []:
            answer.append(list1[2].pop(0))
      if list1[3] != []:
            answer.append(list1[3].pop(0))
      if list1[4] != []:
            answer.append(list1[4].pop(0))
print("".join(answer))