# 토마토
import sys
from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]
m,n = map(int, sys.stdin.readline().split())
a = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]

q = deque()

for i in range(n) :
  for j in range(m) :
    if(a[i][j] > 0) :
      q.append((i,j))

while q:
  y,x = q.popleft()

  for i in range(4) :
    ny = y + dy[i]
    nx = x + dx[i]
    if(ny >= 0 and nx >=0 and ny < n and nx < m and a[ny][nx] == 0) :
      q.append((ny,nx))
      a[ny][nx] = a[y][x] + 1

ans = 0
for i in range(n) :
  if(ans == -1) :
    break
  for j in range(m) :
    if(a[i][j] == 0) :
      ans = -1
      break
    ans = max(ans,a[i][j])

if(ans == -1) :
  print(ans)
else :
  print(ans-1)