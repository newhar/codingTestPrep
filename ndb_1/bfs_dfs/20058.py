# 21:30 ~ 23:15 1solved
# 20058 마법사상어와 파이어스톰
import sys
import math
from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]

n, q = map(int, sys.stdin.readline().split())
a = []

aLen = int(math.pow(2,n))
for i in range(aLen) :
  a.append(list(map(int, sys.stdin.readline().split())))
magic = list(map(int, sys.stdin.readline().split())) 

def melt() :
  willBeMelted = []
  for y in range(aLen) :
    for x in range(aLen) :
      if(a[y][x] > 0) :
        adjCnt = 0
        for i in range(4) :
          ny = y + dy[i]
          nx = x + dx[i]
          if(ny >= 0 and ny < aLen and nx >= 0 and nx < aLen and a[ny][nx] > 0) :
            adjCnt += 1
        if(adjCnt < 3) :
          willBeMelted.append((y,x))
  for (y,x) in willBeMelted :
    a[y][x] -= 1
  return

def bfs(y,x) :
  q = deque()
  q.append((y,x))
  check[y][x] = True
  areaSize = 1
  while q :
    (y,x) = q.popleft()
    for i in range(4) :
      ny = y + dy[i]
      nx = x + dx[i]
      if(ny >= 0 and ny < aLen and nx >= 0 and nx < aLen and a[ny][nx] > 0 and check[ny][nx] == False) :
        q.append((ny,nx))
        check[ny][nx] = True
        areaSize += 1
  
  return areaSize

def rotate(cy, cx, l) :
  temp = []
  for y in range(cy, cy+l) :
    t = []
    for x in range(cx, cx+l) :
      t.append(a[y][x])
    temp.append(t)

  rotatedTemp = [[0]*l for _ in range(l)]
  for y in range(l) :
    for x in range(l) :
      rotatedTemp[x][l-y-1] = temp[y][x]

  for y in range(l) :
    for x in range(l) :
      a[y+cy][x+cx] = rotatedTemp[y][x]
  
  
for l in magic : 
  l = int(math.pow(2, l))
  for y in range(aLen) :
    for x in range(aLen) :
      if( y % l == 0 and x % l == 0) :
        rotate(y,x,l)    
  melt()
  
totalIce = 0
maxAreaRange = 0
check = [ [ False for _ in range(aLen)] for _ in range(aLen)]
for y in range(aLen) :
  for x in range(aLen) :
    totalIce += a[y][x]
    if(a[y][x] > 0 and check[y][x] == False) :
      maxAreaRange = max(maxAreaRange, bfs(y,x))
      
print(totalIce)
print(maxAreaRange)