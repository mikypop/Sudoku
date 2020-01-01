import pygame, sys
from settings import *


class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = testBoard
        print(self.grid)

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        self.window.fill(WHITE)
        self.drawGrid(self.window)
        pygame.display.update()

    def drawGrid(self, window):
        pygame.draw.rect(window, BLACK, (gridPos[0], gridPos[1], WIDTH - GRIDDING, HEIGHT - GRIDDING), 2)
        for x in range(sizeSquared):
            if x % size != 0:
                pygame.draw.line(window, BLACK, (gridPos[0] + (x*cellSize), gridPos[1]), (gridPos[0] + (x*cellSize), gridPos[1] + LINING))
                pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1] + (x * cellSize)), (gridPos[0] + LINING, gridPos[1] + (x * cellSize)))
            else:
                pygame.draw.line(window, BLACK, (gridPos[0] + (x * cellSize), gridPos[1]), (gridPos[0] + (x * cellSize), gridPos[1] + LINING), 2)
                pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1] + (x * cellSize)), (gridPos[0] + LINING, gridPos[1] + (x * cellSize)), 2)
