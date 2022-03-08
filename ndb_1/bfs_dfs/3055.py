#3055 탈출 (14:15 ~ 15:10 실패)
#(16:00 ~ )
import sys
from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]

r,c = map(int,sys.stdin.readline().split())
a = []
for _ in range(r) :
  a.append( list(sys.stdin.readline().strip()))
w = [[-1] * c for _ in range(r)]
cost = [[-1] * c for _ in range(r) ]
def expand() :
  waters = deque()
  for i in range(r) :
    for j in range(c) :
      if(a[i][j] == '*') :
        waters.append((i,j))
        w[i][j] = 0
      
  while waters :
    (y,x) = waters.popleft()
    for i in range(4) :
      ny = y + dy[i]
      nx = x + dx[i]
      if nx < 0 or ny < 0 or nx >= c or ny >= r:
        continue
      if a[ny][nx] != '.' :
        continue
      if w[ny][nx] != -1 :
        continue
      w[ny][nx] = w[y][x] + 1
      waters.append((ny,nx))

def bfs() :
  q = deque()
  
  for i in range(r) :
    for j in range(c) :
      if(a[i][j] == 'S') :
        q.append((i,j))
        cost[i][j] = 0
  
  while q :
    (y,x) = q.popleft()
    for i in range(4) :
      ny = y + dy[i]
      nx = x + dx[i]
      if nx < 0 or ny < 0 or nx >= c or ny >= r:
        continue
      if a[ny][nx] != '.' and a[ny][nx] != 'D':
        continue
      if w[ny][nx] != -1 and w[ny][nx] <= cost[y][x] + 1 :
        continue
      if cost[ny][nx] != -1 :
        continue
      cost[ny][nx] = cost[y][x] + 1
      q.append((ny,nx))
  
expand()
bfs()

for i in range(r) :
  for j in range(c) :
    if(a[i][j] == 'D') :
      if(cost[i][j] == -1) :
        print("KAKTUS")
      else :
        print(cost[i][j])