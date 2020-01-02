WIDTH = HEIGHT = 600
START = HEIGHT * (3/4)
END = HEIGHT / 4

size = int(input("Enter size for Sudoku game:\n"))
sizeSquared = size * size


# Colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
LIGHTBLUE = 0x61F4FF

# Boards
testBoard = [[0 for x in range(sizeSquared)] for x in range(sizeSquared)]


# Positions and sizes
gridPos = (0.125 * WIDTH, (1/6) * HEIGHT)
cellSize = START / sizeSquared
gridSize = cellSize * sizeSquared