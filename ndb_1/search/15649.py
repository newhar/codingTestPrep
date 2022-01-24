# 23:45 ~ 23:55
import sys
n, m = map(int, sys.stdin.readline().split())

selected = [0 for _ in range(m)]
check = [False for _ in range(n+1)]

def go(idx) :
  if(idx == m) :
    for x in selected :
      sys.stdout.write(str(x) + ' ')
    sys.stdout.write('\n')  
    return

  for i in range(1, n+1) :
    if(check[i] == True) :
      continue
    selected[idx] = i
    check[i] = True
    go(idx+1)
    selected[idx] = 0
    check[i] = False
  
go(0)
