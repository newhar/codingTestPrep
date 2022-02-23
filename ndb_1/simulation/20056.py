# 15:50 ~ 18:00 (2h 10min)
#  20056 마법사상어와 파이어볼
# 다풀었는데 조건중 하나 잘못읽어서 (모두 홀수거나 모두 짝수일때인데 맘대로 해석했음)
# 다음부터는 구현위주의 코드를 풀때는 지문과 구현을 하나하나 맵핑하며 검토할 필요가 있다.
import sys
dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]

n,m,k = map(int, sys.stdin.readline().split())
a =  [[ [] for _ in range(n)] for _ in range(n)]

def move() :
  ballsAfterMove = [[ [] for _ in range(n) ] for _ in range(n)]
  for y in range(n) :
    for x in range(n) :
      if(a[y][x] != []) :
        for ball in a[y][x] :
          ny = ( y + dy[ball[2]] * ball[1] ) % n
          nx = ( x + dx[ball[2]] * ball[1] ) % n 
          ballsAfterMove[ny][nx].append([ball[0],ball[1],ball[2]])
  
  return ballsAfterMove

def merge() :
  ballsAfterMerge = [[ [] for _ in range(n) ] for _ in range(n)]
  for y in range(n) :
    for x in range(n) :
      if(len(a[y][x]) > 1) :
        mass = 0
        speed = 0
        oddCnt = 0
        evenCnt = 0
        for ball in a[y][x] :
          if(ball[2] % 2 == 1) :
            oddCnt += 1
          else :
            evenCnt += 1
          mass += ball[0]
          speed += ball[1]
        
        if(int(mass / 5) > 0) :
          for i in range(0,8, 2) :
            if(oddCnt == len(a[y][x]) or evenCnt == len(a[y][x])) :
              ballsAfterMerge[y][x].append([int(mass/5), int(speed/len(a[y][x])),i])
            else :
              ballsAfterMerge[y][x].append([int(mass/5), int(speed/len(a[y][x])),i+1])

      elif(len(a[y][x]) == 1) :
        ballsAfterMerge[y][x].append(a[y][x][0])
  return ballsAfterMerge

for _ in range(m) :
  r,c,m,s,d = map(int, sys.stdin.readline().split())
  a[r-1][c-1].append([m,s,d])

for i in range(k) :
  a = move()
  a = merge()

ans = 0
for y in range(n) :
  for x in range(n) :
    if(a[y][x] != [] ) :
      for ball in a[y][x] :
        ans += ball[0]

print(ans)