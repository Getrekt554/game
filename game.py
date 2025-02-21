import pygame

pygame.init()
screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()
run  = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    clock.tick(60)

pygame.quit()