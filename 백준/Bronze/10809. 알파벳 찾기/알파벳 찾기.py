import string 
alphabet=list(string.ascii_lowercase)
a = input()
for i in alphabet:
  print(a.find(i), end = " ")
print("")