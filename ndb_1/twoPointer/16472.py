#16472 고냥이 18:20 ~ 18:43
import sys
from collections import deque

n = int(sys.stdin.readline())
a = sys.stdin.readline()

q = deque()
r = 0
ans = 0
check = [0] * 26
kind = 0

for l in range(len(a) - 1) :
  if q :
    c = ord( q.popleft() ) - ord('a')
    check[c]  -= 1
    if(check[c] == 0) : 
      kind -= 1
    
  while( r < len(a) - 1 ) :
    c = ord(a[r]) - ord('a')
    if(check[c] == 0 and kind == n ) :
      break
    q.append(a[r])
    if(check[c] == 0) :
      kind += 1
    check[c] += 1    
    r += 1  
    
  ans = max( ans, len(q) )

print(ans)
    
    
