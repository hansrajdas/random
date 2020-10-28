def get_new_perms(perm, c):
    permutations = []
    for i in range(len(perm) + 1):
        permutations.append(perm[:i] + c + perm[i:])
    return permutations
    
def computePermutationsUniqueChars(string):
    if len(string) < 2:
        return string
    perms = computePermutationsUniqueChars(string[1:])
    new_char = string[0]
    new_permutations = []
    for perm in perms:
        new_permutations.extend(get_new_perms(perm, new_char))
    return new_permutations

def main():
  string = input('Enter input string(having unique characters): ')
  permutations = computePermutationsUniqueChars(string)
  for idx in range(len(permutations)):
    print('{idx}: {perm}'.format(idx=idx + 1, perm=permutations[idx]))

if __name__ == '__main__':
  main()

