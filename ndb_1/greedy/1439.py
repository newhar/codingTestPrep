# 15:50 ~ 16:02 , 1 solved
# 백준 1439 뒤집기 (S5)
s = input()

def solution(str) :  
  if(len(str) == 1) :
    print(0)
    return
  cur = '-1'
  cnt = [0,0]
  for c in str :
    if(c == cur) :
      continue
    else :
      cnt[int(c)] += 1
      cur = c
  print(min(cnt))
  return

solution(s)
