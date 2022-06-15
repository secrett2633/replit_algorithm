import sys
input = sys.stdin.readline
import datetime
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
time = list(input().split())
time[1] = time[1][:-1]
date = datetime.datetime(int(time[2]), int(month.index(time[0])+1), int(time[1]), int(time[3][:2]), int(time[3][3:]))
diff = date - datetime.datetime(int(time[2]), 1, 1, 0, 0, 0)

if int(time[2]) % 400 == 0 or (int(time[2]) % 100 != 0 and int(time[2]) % 4 == 0):
    print((diff.total_seconds()/31622400) * 100)
else:
    print((diff.total_seconds()/31536000) * 100)