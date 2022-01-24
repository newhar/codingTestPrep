import sys

n,m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

selected = [0 for _ in range(m)]
checked = [False for _ in range(len(a))]

def go(idx) :
  if(idx == m) :
    for x in selected :
      sys.stdout.write(str(x) + ' ')
    sys.stdout.write('\n')
    return

  prev = -1
  for i in range(n) :
    if(checked[i] == True or prev == a[i]) :
      continue
    prev = a[i]
    
    selected[idx] = a[i]
    checked[i] = True
    go(idx+1)
    selected[idx] = 0
    checked[i] = False

go(0)