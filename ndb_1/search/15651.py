# 23:13 ~ 23:30
import sys
n, m = map(int, sys.stdin.readline().split())

selected = [0 for _ in range(m)]

def go(l) :
  if(l == m) :
    for x in selected :
      sys.stdout.write(str(x) + ' ')
    sys.stdout.write('\n')  
    return

  for i in range(1, n+1) :
    selected[l] = i
    go(l+1)
    selected[l] = 0
  
go(0)


