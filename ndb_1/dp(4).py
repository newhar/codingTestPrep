# dp4
# 22:38 ~ 23:00

for _ in range(int(input())) :
  n,m = map(int, input().split())
  a = list(map(int, input().split()))

  d = []
  index = 0
  for i in range(n) :
    d.append(a[index:index+m])
    index += m
  
  for j in range(1,m) :
    for i in range(n) :
      if i == 0 : left_up = 0
      else : left_up = d[i-1][j-1]

      if i == n-1 : left_down = 0
      else: left_down = d[i+1][j-1]

      left = d[i][j-1]
      d[i][j] = d[i][j] + max(left_up, left_down, left)
  
  result = 0
  for i in range(n) :
    result = max(result, d[i][m-1])
  
  print(result)

