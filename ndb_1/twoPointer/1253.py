# 1253 좋다
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

a.sort()
cnt = 0
for i in range(n) :
  l = 0
  r = n-1
  while ( l < r ) :
    if(l == i) : 
      l += 1
    elif(r == i) : 
      r -= 1
    else :
      twoSum = a[l]+a[r]
      if(twoSum < a[i]) :
        l += 1
      elif(twoSum > a[i]) :
        r -= 1
      else :
        cnt += 1
        break

print(cnt)
