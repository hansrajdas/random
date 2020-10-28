#!/usr/bin/python

# Date: 2018-08-05
#
# Description:

import enum
import collections

class Colors(enum.Enum):
  GREEN = 'GREEN'
  BLACK = 'BLACK'
  BLUE = 'BLUE'
  RED = 'RED'

def paintFillWithNewColorBFS(screen, row, col, oldColor, newColor):
    Q = collections.deque()
    Q.append((row, col))
    while Q:
        row, col = Q.popleft()
        if row < 0 or col < 0 or row >= len(screen) or col >= len(screen[0]):
            continue
        if screen[row][col] == oldColor:
            screen[row][col] = newColor
            Q.append((row - 1, col))
            Q.append((row + 1, col))
            Q.append((row, col - 1))
            Q.append((row, col + 1))

def paintFill(screen, row, col, newColor):
    if screen[row][col] == newColor:
        return
    paintFillWithNewColorBFS(screen, row, col, screen[row][col], newColor)

def main():
  # 3x2 screen, filled with few colors
  screen = [
    [Colors.BLUE.value, Colors.BLUE.value],
    [Colors.BLUE.value, Colors.BLACK.value],
    [Colors.BLUE.value, Colors.BLACK.value],
  ]

  # Row and col index which is clicked, new color = RED.
  row = 0
  col = 0
  paintFill(screen, row, col, Colors.RED.value)
  
  print('********* Updated matrix **********')
  for rowIdx in range(len(screen)):
    print(screen[rowIdx])

if __name__ == '__main__':
  main()

# Output:
# ********* Updated matrix **********
# ['RED', 'RED']
# ['RED', 'BLACK']
# ['RED', 'BLACK']

