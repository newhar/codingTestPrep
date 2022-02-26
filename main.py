# 15:20 ~ 18:20 
# 21609 상어중학교 (16:33 ~ 18:15 1h 45min 1 solved)
# 두문제 모두 한번에 모두 통과 2h 45min 소요.

import sys
import math
from collections import deque
# 격자가 90도 반시계 방향으로 회전한다.
# 다시 격자에 중력이 작용한다.

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y, x) :
  # 그룹에 속한 블록의 개수는 2보다 크거나 같아야 하며, 임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다. 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록이다.
  # 시작점이 기준블록일 수 밖에 없다. 인접하는 최상단이기 때문.  
  bCnt, rCnt = 1,0
  tempCheckList = []
  rainbowCheckList = []
  normBlockNum = a[y][x]

  q = deque()
  q.append((y,x))
  check[y][x] = True
  tempCheckList.append((y,x))

  while q :
    (y,x) = q.popleft()
    for i in range(4) :
      ny = y + dy[i]
      nx = x + dx[i]
      if(ny >= 0 and ny < n and nx >= 0 and nx < n and check[ny][nx] == False) :
        if(a[ny][nx] == 0) :
          check[ny][nx] = True
          tempCheckList.append((ny,nx))
          rainbowCheckList.append((ny,nx))
          q.append((ny,nx))
          rCnt += 1
        elif(a[ny][nx] == normBlockNum) :
          check[ny][nx] = True
          tempCheckList.append((ny,nx))
          q.append((ny,nx))
          bCnt += 1

  if(bCnt + rCnt < 2) :
    for (y,x) in tempCheckList :
      check[y][x] = False
  else :
    for (y,x) in rainbowCheckList :
      check[y][x] = False
  return (bCnt,rCnt)

def removeBlock(group) :
  score = int(math.pow(group[0] + group[1], 2))
  (y,x) = (group[2],group[3])
  
  blockNum = a[y][x]
  q = deque()
  tCheck = [[False] * n for _ in range(n)]
  q.append((group[2], group[3]))
  tCheck[group[2]][group[3]] = True
  a[y][x] = -2

  while q :
    (y,x) = q.popleft()
    for i in range(4) :
      ny = y + dy[i]
      nx = x + dx[i]
      if(ny >= 0 and ny < n and nx >=0 and nx <n and tCheck[ny][nx]==False) :
        if(a[ny][nx] == 0 or a[ny][nx] == blockNum) :
          tCheck[ny][nx] = True
          a[ny][nx] = -2
          q.append((ny,nx))
  return score
  
def gravity() :
  # 모든 칸에 대하여-2 일때만 내릴 수 있으면된다. -1 이면 이동하면 안됨.
  for _ in range(n) :
    for y in range(n) :
      for x in range(n) :
        if(a[y][x] == -1) : continue
        ny = y + 1
        if(ny < n and a[ny][x] == -2) :
          a[ny][x] = a[y][x]
          a[y][x] = -2
  return

def rotate() :
  temp = [[0] * n for _ in range(n)]
  for y in range(n) :
    for x in range(n) :
      temp[n-1-x][y] = a[y][x] 

  return temp

n,m = map(int,sys.stdin.readline().split())
a = []
ans = 0
for _ in range(n) :
  a.append( list(map(int, sys.stdin.readline().split())) )

# 크기가 가장 큰 블록 그룹을 찾는다. 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹, 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그 것도 여러개이면 열이 가장 큰 것을 찾는다.
check = [ [False] * n for _ in range(n) ]

while True :
  
  check = [ [False] * n for _ in range(n) ]
  candid = [] # (blockCnt, rainbowCnt, minY, minX )
  
  for y in range(n) :
    for x in range(n) :
      if(check[y][x] == False and a[y][x] > 0) :
        (blockCnt, rainbowCnt) = bfs(y,x)
        if(blockCnt + rainbowCnt >= 2) :
          candid.append( (blockCnt,rainbowCnt, y, x) )
  
  if(candid == []) :
    break
  
  candid.sort(key = lambda x : (-(x[0]+x[1]), -x[1], -x[2], -x[3]))
  # 1에서 찾은 블록 그룹의 모든 블록을 제거한다. 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B2점을 획득한다.
  ans += removeBlock(candid[0])
  gravity()
  a = rotate()
  gravity()  

print(ans)



      