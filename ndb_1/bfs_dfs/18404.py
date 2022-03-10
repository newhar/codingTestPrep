#18404 현명한 나이트의 이동
import sys
from collections import deque
sr = sys.stdin.readline

dy,dx = [-2,-1,1,2,2,1,-1,-2],[1,2,2,1,-1,-2,-2,-1]
n,m  = map(int, sr().split())
sy,sx = map(int, sr().split())

enemy = [ [0] * (n+1) for _ in range(n+1)]
for i in range(1,m+1) :
  ey,ex = map(int, sr().split())
  enemy[ey][ex] = i

a = [ [0] * (n+1) for _ in range(n+1) ]

q = deque()
q.append((sy,sx))

ans = [0] * m
totalCnt = 0
while q :
  (y,x) = q.popleft()
  if(enemy[y][x] > 0) :
    ans[enemy[y][x]-1] = a[y][x]
    totalCnt += 1
    if(totalCnt == m) :
      break
      
  for i in range(8) :
    ny = y + dy[i]
    nx = x + dx[i]
    if(ny>=1 and nx>=1 and ny<n+1 and nx<n+1 and a[ny][nx] == 0) :
      a[ny][nx] = a[y][x] + 1
      q.append((ny,nx))

print(*ans)