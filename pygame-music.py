import pygame
from pygame.mixer import unpause
pygame.mixer.init()
pygame.init()

size = [400, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Music in Pygame')
white = ('#ffffff')
font = pygame.font.Font(None, 15)

pygame.mixer.music.load('pygame-music.mp3')

vol = 1
pause = False
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                pygame.mixer.music.play()
            elif event.key == pygame.K_2:
                if pause == False:
                    pygame.mixer.music.pause()
                    pause = True
                else:
                    pygame.mixer.music.unpause()
                    pause = False
            elif event.key == pygame.K_r:
                pygame.mixer.music.rewind()
            elif event.key == pygame.K_3:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_UP:
                vol += 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.key == pygame.K_DOWN:
                vol -= 0.1
                pygame.mixer.music.set_volume(vol)

    screen.fill(white)
    pygame.display.update()
