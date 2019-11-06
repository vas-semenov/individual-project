import pygame
import sys

size = width, height = 2560, 1600
black = 0, 0, 0

def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    gameover = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.quit():
                gameover = True
        screen.fill(black)
        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()

main()