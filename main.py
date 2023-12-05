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

    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    bg1, bg2, gameover_img, flappybird_img = load_images()

    bg = random.choice([bg1, bg2])

    im_list = [pygame.image.load('Assets/pipe-green.png'), pygame.image.load('Assets/pipe-red.png')]
    pipe_img = random.choice(im_list)

    pipe_group = pygame.sprite.Group()
    base = Base(win)
    score_img = Score(WIDTH // 2, 50, win)
    bobby = Bobby(win)

    base_height = 0.80 * HEIGHT
    speed = 0
    game_started = False
    game_over = False
    restart = False
    score = 0
    start_screen = True
    pipe_pass = False
    pipe_frequency = 2000

    running =  True
    while running:
        win.blit(bg, (0,0))

        if start_screen:
            speed = 0
            bobby.draw_flap()
            base.update(speed)
            win.blit(flappybird_img, (40, 50))
        else:
            if game_started and not game_over:
                next_pipe = pygame.time.get_ticks()
                if next_pipe - last_pipe >= pipe_frequency:
                    y = display_height // 2
                    pipe_pos = random.choice(range(-100,100,4))
                    height = y + pipe_pos

                    top = Pipe(win, pipe_img, height, 1)
                    bottom = Pipe(win, pipe_img, height, -1)
                    pipe_group.add(top)
  

            if bobby.rect.bottom >= display_height:
                speed = 0
                game_over = True

            if len(pipe_group) > 0:
                p = pipe_group.sprites()[0]
                if bobby.rect.left > p.rect.left and bobby.rect.right < p.rect.right and not pipe_pass and bobby.alive:
                    pipe_pass = True

                if pipe_pass:
                    if bobby.rect.left > p.rect.right:
                        pipe_pass = False
                        score += 1

        if not bobby.alive:
            win.blit(gameover_img, (50, 200))

        for event in pygame.event.get():
            if event.type in (pygame.QUIT, pygame.KEYDOWN):
                if event.type == pygame.QUIT or event.key in (pygame.K_ESCAPE, pygame.K_q):
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN and start_screen:
                game_started = True
                speed = 2
                start_screen = False
                game_over = False
                last_pipe = pygame.time.get_ticks() - pipe_frequency
                next_pipe = 0
                pipe_group.empty()
                speed = 2
                score = 0

            if game_over and event.type == pygame.MOUSEBUTTONDOWN:
                start_screen = True
                bobby = Bobby(win)
                pipe_img = random.choice(im_list)
                bg = random.choice([bg1, bg2])

        clock.tick(FPS)
        pygame.display.update()
        await asyncio.sleep(0)

    pygame.quit()

asyncio.run(main())
