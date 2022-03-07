# 3273 두수의 합 (16:00 ~ 16:20)
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
a.sort()
ans = 0
l = 0
r = n-1
while(l < r) :
  if (a[l] + a[r] == x) :
    ans += 1
  if (a[l] + a[r] > x) :
    r -= 1
  else :
    l += 1
    
print(ans)
