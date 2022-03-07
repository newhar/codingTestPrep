#2003 수들의 합2 (13:21 ~ 13:50 )
import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

sum = 0
ans = 0
r = 0 # r : right side of two pointer
for l in range(n) : # l : left side of two pointer
   
  while( r < n and sum < m ) :
    # put an element in subSumQueue until over 'm'
    sum += a[r]
    r += 1
    
  if(sum == m) :
    ans += 1
    
  sum -= a[l]

print(ans)
    