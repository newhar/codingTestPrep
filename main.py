# 15:52 ~ 16:02
nums = input()

l = int(nums[0])
for idx in range(1, len(nums)) :
  r = int(nums[idx])
  if(l <= 1 or r <= 1) :
    l += r
  else :
    l *= r

print(l)