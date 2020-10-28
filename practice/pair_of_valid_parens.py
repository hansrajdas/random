def generatePairOfParens(left_rem, right_rem, holder, idx, resp):
    if left_rem < 0 or right_rem < left_rem:
        return
    if not (left_rem or right_rem):
        resp.append(''.join(holder))
    else:
        if left_rem > 0:
            holder[idx] = '('
            generatePairOfParens(left_rem - 1, right_rem, holder, idx + 1, resp)
        if right_rem > left_rem:
            holder[idx] = ')'
            generatePairOfParens(left_rem, right_rem - 1, holder, idx + 1, resp)

def main():
  n = int(input("Enter n: "))
  parens = []
  holder = [''] * n * 2
  generatePairOfParens(n,  # Left paren remaining
                       n,  # Right paren remaining
                       holder,  # Dummy to have parens place holders
                       0,       # Counter for holder
                       parens)  # Response
  for idx, paren in enumerate(parens, 1):
    print(f'{idx}: {paren}')

if __name__ == '__main__':
  main()
