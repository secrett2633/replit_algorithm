n = int(input())
count = 0
stack = []
result = []
no_message=True
arr = []
for i in range(n):
    arr.append(int(input()))
  
for i in range(0,n):
    x = arr[i]
  
    while count < x:
      count += 1
      stack.append(count)
      result.append("+")

    if stack[-1]==x:
        stack.pop()
        result.append("-")
    else:
        no_message = False
        break

if no_message==False:
    print("NO")
else:
    print("\n".join(result))