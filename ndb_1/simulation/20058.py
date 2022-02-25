# 13:55 ~ 16:25 (2h 30min)
# 마법상어와 토네이도
import sys
import math

dy = [0,1,0,-1]
dx = [-1,0,1,0]
n = int(sys.stdin.readline())
a = []
ratioMap = [
  [(0,-3,5), (-1,-2,10), (1,-2,10), (-2,-1,2), (-1,-1,7),(1,-1,7),(2,-1,2),(-1,0,1),(1,0,1),(0,-2,55)],
  [(3, 0, 5), (2, 1, 10), (2, -1, 10), (1, 2, 2), (1, 1, 7), (1, -1, 7), (1, -2, 2), (0, 1, 1), (0, -1, 1), (2, 0, 55)],
             [(0, 3, 5), (-1, 2, 10),  (1, 2, 10), (-2, 1, 2), (-1, 1, 7), (1, 1, 7), (2, 1, 2), (-1, 0, 1), (1, 0, 1), (0, 2, 55)],
  [(-3, 0, 5), (-2, 1, 10), (-2, -1, 10), (-1, 2, 2), (-1, 1, 7), (-1, -1, 7), (-1, -2, 2), (0, 1, 1), (0, -1, 1), (-2, 0, 55)]
           ]

def tornado() :
  ans = 0
  y,x = int(n/2), int(n/2)  
  for i in range(1, n*2) :
    dist = math.ceil(i/2)
    dir = (i-1) % 4
    if(dist == n) :
      dist = n-1
    for j in range(dist) :
      ny = y + dy[dir]
      nx = x + dx[dir]
      initSand = a[y][x] + a[ny][nx]
      leftSand = initSand
      a[ny][nx] = 0
      for ratio in ratioMap[dir] :
        ny = y + ratio[0]
        nx = x + ratio[1]
        if(ratio[2] == 55) :
          spradedSand = leftSand

          if(ny >= 0 and ny < n and nx >= 0 and nx < n) :
            a[ny][nx] += spradedSand
          else :
            ans += spradedSand
            
        else :
          spradedSand = math.floor(initSand * ratio[2] / 100)
          leftSand -= spradedSand
          
          if(ny >= 0 and ny < n and nx >= 0 and nx < n) :
            a[ny][nx] += spradedSand
          else :
            ans += spradedSand
      
      y = y + dy[dir]
      x = x + dx[dir]
  print(ans)
  return 
  
for _ in range(n) :
  a.append( list( map(int, sys.stdin.readline().split()) ) )

tornado()