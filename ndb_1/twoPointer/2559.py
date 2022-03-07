#2003 수들의 합2 (13:21 ~ 13:50 )
import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

sum = 0
r = 0
ans = -987654321
size = 0
for l in range(n - k + 1) :

  while( r < n and size < k) :
    sum += a[r]
    size += 1
    r += 1

  ans = max(ans, sum)
  
  sum -= a[l]
  size -= 1

print(ans)
    