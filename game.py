import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
run  = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()