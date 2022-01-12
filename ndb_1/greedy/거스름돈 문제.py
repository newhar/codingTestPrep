n = 1260
count = 0

arr = [500,100,50,10]

for coin in arr :
  count += n // coin
  n %= coin

print(count)