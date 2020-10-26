def can_reach_origin(r, c, maze, memo, path):
    if r < 0 or c < 0 or not maze[r][c]:
        return False
    if (r, c) in memo:
        return memo[(r, c)]
    reached_origin = not (r | c)
    status = False
    if (reached_origin or can_reach_origin(r - 1, c, maze, memo, path) or
        can_reach_origin(r, c - 1, maze, memo, path)):
        path.append((r, c))
        status = True
    memo[(r, c)] = status
    return memo[(r, c)]

def robotInAGrid(maze):
    r = len(maze) - 1
    c = len(maze[0]) - 1

    memo = {}
    path = []
    if can_reach_origin(r, c, maze, memo, path):
        return path
    return None

def main():
  maze_1 = [
    [1, 1, 0],
    [0, 1, 0],
    [1, 1, 1],
  ]
  maze_2 = [
    [1, 0, 1],
    [0, 0, 1],
    [1, 1, 0],
    [0, 0, 1],
  ]
  maze_3 = [
    [1, 1, 1],
    [0, 0, 1],
    [0, 0, 1],
    [0, 0, 1],
  ]
  mazes = [maze_1, maze_2, maze_3]
  for maze in mazes:
    path = robotInAGrid(maze)
    if path:
      print('Path form top-left to bottom-right is:', '=>'.join(map(str, path)))
    else:
      print('Path from top-left to bottom-right does *NOT* exist')

if __name__ == '__main__':
  main()

# Output:
# Path form top-left to bottom-right is: (0, 0)=>(0, 1)=>(1, 1)=>(2, 1)=>(2, 2)
# Path from top-left to bottom-right does *NOT* exist
# Path form top-left to bottom-right is: (0, 0)=>(0, 1)=>(0, 2)=>(1, 2)=>(2, 2)=>(3, 2)
