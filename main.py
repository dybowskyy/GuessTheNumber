import pygame as pg
import random
import sys

from pygame.examples.moveit import WIDTH, HEIGHT

pg.init()
pg.font.init()
font = pg.font.SysFont("comicsansms", 80)

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 650
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
RED = (255, 0, 0)

def main():
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    num_target = 0
    user_input = ""
    attempts = 0
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    running = True
    while running:
        num_target = random.randint(1, 10)
        for event in pg.event.get():
            if event.type == pg.QUIT:  # Correctly check for QUIT event
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            elif event.type == pg.KEYDOWN:
                if chr(event.key).isdigit():
                    user_input += chr(event.key)
                if event.key == pg.K_RETURN:
                    print(f'Output {user_input}')
                    user_input = int(user_input)
                    if user_input == num_target:
                        attempts += 1
                        print(f'You guessed correctly! {num_target} was the correct number!')
                        print(f'It took you {attempts} tries to get the number right')
                    else:
                        print("You guessed wrong! Try again")
                        attempts += 1
                    user_input = ""


        screen.fill(BLACK)
        pg.display.flip()

    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
