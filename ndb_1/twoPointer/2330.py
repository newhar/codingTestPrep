# 2330 수고르기 (14:20 ~ 15:20)
import sys

n, m = map(int, sys.stdin.readline().split())

a = []
for _ in range(n) :
  a.append(int(sys.stdin.readline()))

a.sort()

ans = 1 << 31

r = 0
for l in range(n-1) :
  while (r+1 < n and a[r]-a[l] < m) :
    r += 1

  if(a[r]-a[l] >= m ) :
    ans = min(ans , a[r]-a[l])

print(ans)