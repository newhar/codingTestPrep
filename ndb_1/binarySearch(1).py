# 숫자개수 찾기
# 19:58 ~ 20:02
from bisect import bisect_left, bisect_right

n, target = map(int, input().split(' '))
a = list(map(int, input().split()))

l = bisect_left(a, target)
r = bisect_right(a, target)

if(r-l == 0) :
  print(-1)
else :
  print(r-l)


