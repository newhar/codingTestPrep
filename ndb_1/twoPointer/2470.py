#2470 두용액
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

def twoPointer() :
  l = 0
  r = n-1
  twoSum = 1 << 31
  v1,v2 = 0,0

  while(l < r) :    
    if(twoSum > abs(a[l]+a[r])) :
      v1,v2 = a[l],a[r]
      twoSum = abs(a[l]+a[r])
      
    if(a[l] + a[r] > 0) :
      r -= 1
    else :
      l += 1
  print(v1,v2)
  
a.sort()
twoPointer()