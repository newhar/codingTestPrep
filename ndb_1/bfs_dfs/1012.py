# 유기농 배추
import sys
from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(row, col) :
  q = deque()
  q.append((row,col));
  while q :
    cy, cx = q.popleft()
    for i in range(4) :
      ny = cy + dy[i]
      nx = cx + dx[i]
      if(ny >= 0 and nx >= 0 and ny < n and nx < m and a[ny][nx] == 1 and check[ny][nx] == 0) :
        check[ny][nx] = 1
        q.append((ny,nx))

t = int(sys.stdin.readline())

while(t > 0) :
  t -= 1
  ans = 0
  n,m,k = map(int, sys.stdin.readline().split());
  a = [[0] * m for _ in range(n)]
  check = [[0] * m for _ in range(n)]
  for _ in range(k):
    y, x = map(int, sys.stdin.readline().split());
    a[y][x] = 1

  for i in range(n) :
    for j in range(m) :
      if(check[i][j] == 0 and a[i][j] == 1) :
        bfs(i,j)
        ans += 1
  print(ans)