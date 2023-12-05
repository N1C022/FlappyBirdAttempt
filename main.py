import pygame
import random
import asyncio
from objects import Bobby, Pipe, Base, Score

def load_images():
    bg1 = pygame.image.load('Assets/background-day.png')
    bg2 = pygame.image.load('Assets/background-night.png')
    gameover_img = pygame.image.load('Assets/gameover.png')
    flappybird_img = pygame.image.load('Assets/flappybird.png')
    flappybird_img = pygame.transform.scale(flappybird_img, (200, 80))

    return bg1, bg2, gameover_img, flappybird_img

async def main():
    pygame.init()
    SCREEN = WIDTH, HEIGHT = 288, 512
    display_height = 0.80 * HEIGHT
    info = pygame.display.Info()

    width = info.current_w
    height = info.current_h

    if width < height:
        win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
    else:
        win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

    clock = pygame.time.Clock()
    FPS = 60



    pygame.quit()

asyncio.run(main())
