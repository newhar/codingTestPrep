# dp1
# 21:45 ~ 21:50
n = int(input())
a = list(map(int,input().split()))

d = [0] * 100
d[0] = a[0]
d[1] = max(a[0],a[1])
for i in range(2, len(a)) :
  if(a[i] + d[i-2] > d[i-1]) :
    d[i] = a[i] + d[i-2]
  else :
    d[i] = d[i-1]

print(d[len(a)-1]); 