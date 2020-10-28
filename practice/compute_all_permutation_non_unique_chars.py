def get_permutations(prefix, rem, _map, result):
    if not rem:
        result.append(prefix)
        return
    for k in _map:
        if _map[k] > 0:
            _map[k] = _map[k] - 1
            get_permutations(prefix + k, rem - 1, _map, result)
            _map[k] = _map[k] + 1

def main():
  string = input('Enter input string: ')
  _map = {}
  for c in string:
    if c in _map:
        _map[c] += 1
    else:
        _map[c] = 1

  result = []
  get_permutations('', len(string), _map, result)
  for idx, v in enumerate(result, 1):
    print(f'{idx}: {v}')

if __name__ == '__main__':
  main()
