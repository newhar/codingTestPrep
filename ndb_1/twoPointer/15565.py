#15565 귀여운 라이언 (14:00~14:10)
import sys
# from collections import deque

n, k = map(int, sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

cnt = 0
ans = 9876543210
r = 0
for l in range(n) :

  while( r < n and cnt < k) :
    if(a[r] == 1) :
      cnt += 1
    r += 1

  if(cnt == k) :
    ans = min(ans, r - l) 

  if(a[l] == 1) :
    cnt -= 1

if ans == 9876543210 : ans = -1
  
print(ans)