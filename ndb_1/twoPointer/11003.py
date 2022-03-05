# 11003 최솟값 찾기
import sys
from collections import deque
n,l = map(int, sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

ans = []
q = deque()
for i in range(n) :
  while q and q[-1][1] > a[i] :
    print("pop : ", q, end="")
    q.pop()
    print("->", q)
  while q and q[0][0] < i-l+1 :
    print("popleft : ", q, end="")
    q.popleft()
    print("-> ", q)
  
  q.append((i, a[i]))
  ans.append(q[0][1])

print(*ans)
