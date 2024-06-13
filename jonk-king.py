import pygame

pygame.display.set_caption('Jonk King')
icon = pygame.image.load('jonk-king.ico')
pygame.display.set_icon(icon)
pygame.init()
width = 1280; vert = 720
screen = pygame.display.set_mode((width, vert))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.display.flip()
clock.tick(60)
pygame.quit()
