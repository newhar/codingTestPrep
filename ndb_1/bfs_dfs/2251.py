#2251 물통 (10:30 ~ 12:00)
import sys

maxWarters = list(map(int, sys.stdin.readline().split()))
states = []
ans = []

def dfs(state) :
  if(state[0] == 0 and state[2] not in ans) :
    ans.append(state[2])

  if(state in states) :
    return

  states.append(state)

  st1 = state[:]
  st2 = state[:]
  st3 = state[:]
  st4 = state[:]
  st5 = state[:]
  st6 = state[:]

  # A -> B
  while(st1[0] > 0 and st1[1] < maxWarters[1]) :
    st1[0] -= 1
    st1[1] += 1  
  dfs(st1)
  # A -> C
  while(st2[0] > 0 and st2[2] < maxWarters[2]) :
    st2[0] -= 1
    st2[2] += 1
  dfs(st2)
  # B -> A
  while(st3[1] > 0 and st3[0] < maxWarters[0]) :
    st3[1] -= 1
    st3[0] += 1
  dfs(st3)
  # B -> C
  while(st4[1] > 0 and st4[2] < maxWarters[2]) :
    st4[1] -= 1
    st4[2] += 1
  dfs(st4)
  # C -> A
  while(st5[2] > 0 and st5[0] < maxWarters[0]) :
    st5[2] -= 1
    st5[0] += 1
  dfs(st5)
  # C -> B
  while(st6[2] > 0 and st6[1] < maxWarters[1]) :
    st6[2] -= 1
    st6[1] += 1
  dfs(st6)
  
dfs([0,0,maxWarters[2]])

ans.sort()
print(*ans)
  