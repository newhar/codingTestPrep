#1172 connected components
import sys
sr = sys.stdin.readline
n, k = map(int, sr().split())

g = [ [] for _ in range(n+1) ]
p = [ i for i in range(0,n+1)]
check = [False] * (n+1)


for _ in range(k) :
  (x, y) = map(int, sr().split())
  g[x].append(y)
  g[y].append(x)

def dfs(i) :
  check[i] = True
  for node in g[i] :
    if(check[node] == False) :
      dfs(node)
  
ans = 0
for i in range(1, n+1) :
  if(check[i] == False) :
    dfs(i)
    ans += 1

print(ans)
