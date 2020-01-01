WIDTH = 1000
HEIGHT = 1000
LINING = HEIGHT * (3/4)
GRIDDING = HEIGHT / 4

size = int(input("Enter size for Sudoku game:\n"))
sizeSquared = size * size

# Colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)

# Boards
testBoard = [[0 for x in range(9)] for x in range(9)]


# Positions and sizes
gridPos = (0.125 * WIDTH, (1/6) * HEIGHT)
cellSize = LINING / (sizeSquared)