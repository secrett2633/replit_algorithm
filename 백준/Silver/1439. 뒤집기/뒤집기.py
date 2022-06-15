import re
s = input()
cnt = re.findall("1+", s)
cnt1 = re.findall("0+", s)
print(min(len(cnt), len(cnt1)))