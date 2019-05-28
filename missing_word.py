# Fractal Analytics
def missingWords(s, t):
  
  missing = []
  a = s. split(' ')
  b = t.split(' ')
  
  i = 0
  j = 0
  while i < len(a):
    if j == len(b):
      missing.append(a[i])
    else:
      if a[i] != b[j]:
        missing.append(a[i])
      else:
        j += 1
    i += 1
  return missing

print missingWords('I am using hackerrank to improve programming', 'am hackerrank to improve')
print missingWords('I like cheese', 'like')
