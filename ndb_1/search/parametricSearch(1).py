# 떡만들기
# 19:27 ~ 19:45
n, target = map(int, input().split())
a = list(map(int, input().split()))

def calc(h) :
  total = 0
  for x in a :
    if(x-h > 0) :
      total += (x-h)
  return total

l = min(a)
r = max(a)
result = 0
while l <= r :
  mid = (l + r) // 2
  cur = calc(mid)
  if(target <= cur) :
    result = mid
    l = mid + 1
  else :
    r = mid - 1

print(result)



