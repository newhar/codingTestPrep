#5567 결혼식
import sys
from collections import deque
sr = sys.stdin.readline

n = int(sr())
m = int(sr())
g = [[] for _ in range(n+1)]
for _ in range(m) :
  a,b = map(int, sr().split())
  g[a].append(b)
  g[b].append(a)

visit = [False] * (n+1)
relation = [0] * (n+1)

q = deque()
q.append(1)
visit[1] = True

while q :
  cur = q.popleft()

  for nextNode in g[cur] :
    if(visit[nextNode] == False) :
      visit[nextNode] = True
      relation[nextNode] = relation[cur] + 1
      q.append(nextNode)
ans = 0
for r in relation :
  if(r > 0 and r <= 2) :
    ans += 1

print(ans)
