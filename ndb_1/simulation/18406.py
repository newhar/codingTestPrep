# 22:38 ~ 22:42
# 백준 18406 럭키스트레이트 (B2)

def solution() :  
  s = input()
  half = int(len(s)/2)
  s1 = s[:half]
  s2 = s[half:]
  sumS1 = 0
  sumS2 = 0
  for i in range(half) :
    sumS1 += int(s1[i]);
    sumS2 += int(s2[i]);

  if(sumS1 == sumS2) : 
    print("LUCKY")
  else :
    print("READY")

solution()
