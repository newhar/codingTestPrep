#1389 cavin bacon
import sys 
sr = sys.stdin.readline

INF = 987654321
n,m = map(int, sr().split())
a = [ [INF] * (n+1) for _ in range(n+1) ]
for _ in range(m) :
  y,x = map(int, sr().split())
  a[y][x] = 1
  a[x][y] = 1

for i in range(n) :
  a[i][i] = 0

for k in range(1,n+1) :
  for i in range(1,n+1) :
    for j in range(1,n+1) :
      if(a[i][j] > a[i][k] + a[k][j]) :
        a[i][j] = a[i][k] + a[k][j]

ans = INF
who = -1

for i in range(1,n+1) :
  total = 0
  for j in range(1, n+1) :
    if(a[i][j] == INF) : continue
    total += a[i][j]

  if(ans > total) :
    ans = total
    who = i

print(who)