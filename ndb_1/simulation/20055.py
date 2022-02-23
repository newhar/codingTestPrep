# 컨베이어벨트 
# 14:20 ~ 15:40 (1h 20min) 1 solve
import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
belt = deque()
for i in range(1,2*n+1) :
  belt.append([i, a[i-1], False])

ans = 0
while True :
  ans += 1
  # print("")
  # print("#",ans)
  # print("초기상태 : " , belt)

  # 1.벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다. 이때 n 위치에 로봇이 있다면 로봇을 내린다.
  belt.rotate(1)
  if(belt[n-1][2] == True) :
    belt[n-1][2] = False
  # print("회전 : ", belt)
  # 2.가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
  for i in range(2*n - 2, 0, -1) :
    if(belt[i][2] == True) :
      # print("로봇 일치 위치 : ", i, belt[i])
    # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
      if(belt[i+1][2] == False and belt[i+1][1] > 0) :
        # print("로봇 다음 위치", i+1, belt[i+1])
        belt[i][2] = False
        belt[i+1][2] = True
        belt[i+1][1] -= 1
  if(belt[n-1][2] == True) :
    belt[n-1][2] = False
  # print("로봇 이동 : ", belt)
  # 3.올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
  if(belt[0][1] > 0) :
    belt[0][1] -= 1
    belt[0][2] = True
  # print("로봇 올리기 : ", belt)
  # 4.내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
  cnt = 0
  # sys.stdout.write("내구도 : ")
  for i in range(0, 2*n) :
    # sys.stdout.write(str(belt[i][1]) + ' ')
    if(belt[i][1] == 0) :
      cnt += 1
  # sys.stdout.write('\n')
  if(cnt >= k) :
    break

print(ans)

