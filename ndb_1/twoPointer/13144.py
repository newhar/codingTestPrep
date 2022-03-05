#13144 List of unique numbers
# in, not in 함수는 O(n) 이므로, check 배열 사용을 선호하자.
# 특정 수열에서의 갯수나 위치 찾는건 투포인터를 고려하자.
# 수열의 개수는 투포인터로도 가능.

import sys
from collections import deque
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

def solution() :
  ans = 0
  r = 0
  seq = deque()
  visit = [ False ] * 100001
  for l in range(n) :
    if seq :
      visit[seq.popleft()] = False
    while r < n and (visit[a[r]] == False) :
      seq.append(a[r])
      visit[a[r]] = True
      r += 1
    ans += r-l
  print(ans)     
  return

solution()