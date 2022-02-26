# 15:20 ~ 18:20 
# 21608 상어초등학교 (15:20 ~ 16:20 1h , 1solved)
# 힙 정렬 사용하는법 익혀두자. 우선순위큐

import sys
import math

dy = [-1,1,0,0]
dx = [0,0,-1,1]

n = int(sys.stdin.readline())
powN = int(math.pow(n,2))

priority = []
for _ in range(powN) :
  priority.append((list(map(int,sys.stdin.readline().split()))))

a = [ [0] * n for _ in range(n)]
for prior in priority :
  candid = []
  for y in range(n) :
    for x in range(n) :
      if(a[y][x] != 0) :
        continue
        
      likeCnt = 0
      blankCnt = 0
      for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]
        if(ny >= 0 and ny < n and nx >= 0 and nx < n) :            
          if(a[ny][nx] == 0) :
            blankCnt += 1
          elif((a[ny][nx] in prior[1:5]) == True) :
            likeCnt += 1
      candid.append( (likeCnt,blankCnt, y,x) )
  candid.sort(key = lambda x : (-x[0],-x[1], x[2], x[3]))
  a[candid[0][2]][candid[0][3]] = prior[0]

temp = [ [] for _ in range(powN+1)]
for prior in priority :
  temp[prior[0]] = prior[1:5]
  
ans = 0
for y in range(n) :
  for x in range(n) :
    person = a[y][x]
    correctCnt = 0
    for i in range(4) :
      ny = y + dy[i]
      nx = x + dx[i]
      if(ny >= 0 and ny < n and nx >= 0 and nx < n and (a[ny][nx] in temp[person]) == True) :
        correctCnt += 1
    if(correctCnt == 1) :
      ans += (correctCnt)
    elif(correctCnt ==2) :
      ans +=  10
    elif(correctCnt == 3) :
      ans +=  100
    elif(correctCnt == 4 ) :
      ans += 1000
      
print(ans)