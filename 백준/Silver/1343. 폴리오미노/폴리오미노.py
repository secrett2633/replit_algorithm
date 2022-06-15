import re
s = input()
cnt = re.findall("X+|\.+", s)
answer = 0
for i in range(len(cnt)):
      if (len(cnt[i]) % 2 == 1 or len(cnt[i]) < 2) and "." not in cnt[i]:
            answer = -1
            break
      elif "." in cnt[i]:
            continue
      elif len(cnt[i]) >= 4:
            temp = ""
            for k in range(len(cnt[i]) // 4):
                  temp+="AAAA"
            for k in range((len(cnt[i]) % 4) // 2):
                  temp+="BB"
            cnt[i] = temp
      elif len(cnt[i]) == 2:
            cnt[i] = "BB"
if answer == -1:
      print(-1)
else:
      print("".join(cnt))