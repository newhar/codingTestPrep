#2644 촌수계산
import sys
sr = sys.stdin.readline

n = int(sr())
a,b = map(int, sr().split())
m = int(sr())

g = [[] for _ in range(n+1)]
for _ in range(m) :
  y,x = map(int, sr().split())
  g[y].append(x)
  g[x].append(y)

ans = -1
visit = [False] * (n+1)
def dfs(node, cnt) :
  global ans
  if(node == b) :
    ans = cnt
    return

  for nextNode in g[node] :
    if(visit[nextNode] == False) :
      visit[nextNode] = True
      dfs(nextNode, cnt+1)

dfs(a, 0)
print(ans)