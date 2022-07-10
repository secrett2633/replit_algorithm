import sys
input = sys.stdin.readline
def rotated(array_2d):
  list_of_tuples = zip(*array_2d[::-1])
  return [list(elem) for elem in list_of_tuples]
answer = [["0010", "1111", "0010"],
    ["0100", "1111", "1000"],
    ["0010", "1111", "0100"],
    ["0001", "1111", "1000"],
    ["0001", "1111", "0100"],
    ["11100", "00111"],
    ["1100", "0111", "0010"],
    ["1100", "0111", "0001"],
    ["0010", "1110", "0011"],
    ["0001", "1111", "0001"],
    ["1100", "0110", "0011"]]
for _ in range(3):
  arr = [list(map(int, input().split())) for _ in range(6)]
  flag = False
  for _ in range(2):
    for _ in range(4):
      for ans in answer:
        for i in range(7 - len(ans)):
          for j in range(7 - len(ans[0])):
            if flag: break
            flag = True
            for k in range(len(ans)):
              if "".join(map(str, arr[i+k][j:j+len(ans[0])])) != ans[k]: flag = False; break
            if flag: print("yes")            
      arr = rotated(arr)
    for i in range(11):
      for j in range(len(answer[i])):
        answer[i][j] = answer[i][j][::-1]
  if not flag: print("no")