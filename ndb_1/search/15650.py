import sys

n,m = map(int, sys.stdin.readline().split(' '))
selected = [0 for _ in range(m)]

def go(idx) :
  if(idx == m) :
    for x in selected :
      sys.stdout.write(str(x) + ' ')
    sys.stdout.write('\n')
    return

  startNum = 1 if idx == 0 else selected[idx-1]+1
  for i in range(startNum,n+1) :
    selected[idx] = i
    go(idx+1)
    selected[idx] = 0
  
go(0)