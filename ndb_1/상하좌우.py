# 22:00 ~ 22:12
n = int(input())
dirs = list(input().split())

m = [[0]*int(n) for _ in range(int(n))]

y = 0
x = 0
dy = [-1,1,0,0]
dx = [0,0,-1,1]
dics = {'U' : 0, 'D' : 1, 'L' : 2, 'R' : 3}
for dir in dirs :
  ny = y + dy[dics[dir]]
  nx = x + dx[dics[dir]]
  if(ny < 0 or ny >= n or nx < 0 or ny >= n) :
    continue
  y = ny
  x = nx

print(y+1,x+1)
