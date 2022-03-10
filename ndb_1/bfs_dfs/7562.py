#7562 나이트의 이동 (01:06~)
import sys
from collections import deque
sr = sys.stdin.readline

dy,dx = [-2,-1,1,2,2,1,-1,-2],[1,2,2,1,-1,-2,-2,-1]
t = int(sr())
for _ in range(t) :
  n = int(sr())
  sy,sx = map(int, sr().split())
  ey,ex = map(int, sr().split())

  # visit = [ [False] * n for _ in range(n)]
  a = [ [0] * n for _ in range(n) ]

  q = deque()
  q.append((sy,sx))

  ans = 0
  while q :
    (y,x) = q.popleft()
    if((y,x) == (ey,ex)) :
      ans = a[y][x]
      break
    for i in range(8) :
      ny = y + dy[i]
      nx = x + dx[i]
      if(ny>=0 and nx>=0 and ny<n and nx<n and a[ny][nx] == 0) :
        a[ny][nx] = a[y][x] + 1
        q.append((ny,nx))

  print(ans)