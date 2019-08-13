def fun(a, b, c=None):
  print (a, b, c)


d = {'a': 1, 'b': 2}
fun(**d)

d = {'a': 1, 'b': 2, 'c': 10}
fun(**d)
