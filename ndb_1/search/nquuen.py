# 9663 N-Queen
# 21:45 ~ 22:10 문제 아이디어 이해 완료.
# 24:10 ~
import sys

n = int(sys.stdin.readline())

row = [0 for _ in range(n)]
cnt = 0

def promising(h, col) :
  for i in range(h) :
    if( row[i] - i == col - h or row[i] + i == col + h or row[i] == col) :
      return False
  return True

def go(idx) :
  global cnt
  
  if (idx == n) :
    cnt += 1
    return

  for i in range(n) :
    row[idx] = i
    if(promising(idx, i)) :
      go(idx+1)

go(0)
print(cnt)
