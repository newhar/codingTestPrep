# 16:09 ~ 16:30
n = input()
a = list(map(int, input().split()))

a.sort()

cnt = 0
groupNum = 0

for i in range(len(a)) :
  groupNum += 1
  if (groupNum >= i) :
    cnt += 1
    groupNum = 0

print(cnt)
