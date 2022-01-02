# 15:28~15:30
def solution(n,k) :
  cnt = 0
  while(n != 1) :
    if( n % k == 0 ) :
      n = n//k
    else :
      n -= 1
    cnt+=1
  print(cnt)
  return cnt

def solution2(n,k) :
  cnt = 0
  while True :
    target = (n//k) * k
    cnt += (n-target)
    n = target
    if( n < k ) :
      break
    n //= k
    cnt += 1
  
  cnt += (n-1)
  return cnt


n,k = map(int, input().split())
result = solution(n,k)
result2 = solution(n,k)