# 1000 -> 17

def numCount(n):
  count = 1
  a = 0
  b = 1
  c = a + b
  while c <= n:
    c = a + b
    a = b
    b = c
    count += 1
  return count

print numCount(1000)
print numCount(8)  # 0 1 1 2 3 5 8
print numCount(0)
