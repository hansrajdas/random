# Fractal Analytics
def arrangeCoins(coins):
 for c in coins:
   last = 1
   for i in range(c, 1, -1):
     if 2*c < i*i + i:
       last = i
   print(last - 1)


arrangeCoins([2, 5, 8, 3])
arrangeCoins([6])
