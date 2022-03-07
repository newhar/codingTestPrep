# 2473 세 용액 (19:00 ~ 20:00)
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

a.sort()

ans = (0,0,0)

for i in range(n-2) :
  target = a[i]
  l = i+1
  r = n-1

  while( l < r ) :
    if( abs(sum(ans)) > abs(target + a[l] + a[r]) or ans == (0,0,0)) :
      ans = (target, a[l], a[r])
    if (target + a[l] + a[r] > 0 ) :
      r -= 1
    else :
      l += 1

print(*ans)
