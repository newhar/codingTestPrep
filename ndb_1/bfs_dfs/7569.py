# 7569 토마토
import sys
from collections import deque
sr = sys.stdin.readline

m,n,h = map(int, sr().split())
a = []
q = deque()
for i in range(h) :
  temp = []
  for j in range(n) :
    temp.append(list(map(int, sr().split())))
  a.append(temp)

dz = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dx = [0,0,0,0,-1,1]

for i in range(h) :
  for j in range(n) :
    for k in range(m) :
      if(a[i][j][k] == 1) :
        q.append((i,j,k))

# map = [[ [0] * m for _ in range(n) ] for _ in range(h)]
while q :
  (z,y,x) = q.popleft()

  for i in range(6) :
    nz = z + dz[i]
    ny = y + dy[i]
    nx = x + dx[i]
    if(nz >= 0 and ny >= 0 and nx >=0 and nz < h and ny < n and nx < m and a[nz][ny][nx] == 0) :
      a[nz][ny][nx] = a[z][y][x] + 1
      q.append((nz,ny,nx))

ans = -1
possible = True
for i in range(h) :
  for j in range(n) :
    for k in range(m) :
      if(a[i][j][k] == 0) :
        possible = False
        break
      ans = max(ans, a[i][j][k])

if possible : 
  print(ans -1)
else :
  print(-1)

