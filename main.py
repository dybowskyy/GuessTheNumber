import pygame
import random
import sys

pygame.init()
pygame.font.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 650
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
RED = (255, 0, 0)

# Game variables
num_target = 0
user_input = 0
attempts = 0

def main():
    running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Correctly check for QUIT event
                running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
