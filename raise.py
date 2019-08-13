try:
  raise ValueError('Wrong value')
except ValueError as e:
  print e
  raise IOError('Something is wrong...')
