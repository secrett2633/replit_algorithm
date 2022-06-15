doc = input()
ser = input()
doc = list(doc)
i = 0
count = 0
while True:
      if len(doc) - i < len(ser):
            break
      else:
            a = 1
            for j in range(len(ser)):
                  if ser[j] == doc[i+j] and a == 1:                        
                        continue
                  else:
                        a = 0
            if a == 1:
                  count += 1
                  i += len(ser)
            else:
                  i += 1
print(count)