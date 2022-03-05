#1806 부분합 
import sys

n,s = map(int, sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

def bruteForce() :
  flag = False
  for l in range(len(a)) :
    if(flag) :
      break
    for i in range(len(a) - l) :
      tempSum = sum(a[i: i+l+1])
      if(tempSum >= s) :
        print(l+1)
        flag = True
        break
  
  if(flag == False) :
    print(0)

def twoPointer() :
  r = 0
  interval_sum = 0
  minLen = 1000000
  for l in range(n) :

    while( interval_sum < s and r < n ) :
      interval_sum += a[r]
      r += 1
    
    if(interval_sum >= s) :
      minLen = min(minLen, r-l)
      
    interval_sum -= a[l]

  if(minLen == 1000000) :
    print(0)
  else :
    print(minLen)

twoPointer()