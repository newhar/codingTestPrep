#3이 포함된 시간
# 22:20 ~ 22:05
h = int(input())

cnt = 0
for i in range(h+1) :
  for j in range(60) :
    for k in range(60) :
      if '3' in str(i) + str(j) + str(k) :
        cnt += 1

print(cnt)
