import sys
def check():
      n = int(sys.stdin.readline())
      case1 = []
      for i in range(n):
            a = sys.stdin.readline().split(" ")
            case1.append([int(a[0]), int(a[1])])
      case1.sort()
      sort_case1 = []
      for i in case1:
            sort_case1.append(i[-1])
      count = 1
      temp = sort_case1[0]
      for i in range(1, len(case1)):
            temp = min(sort_case1[i - 1], temp)
            if sort_case1[i] < temp:
                  count += 1
      return count
for i in range(int(sys.stdin.readline())):
      print(check())