import pygame, sys, ctypes
user32 = ctypes.windll.user32
monitorRes = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

pygame.display.set_caption('Jonk King')
icon = pygame.image.load('jonk-king.ico')
pygame.display.set_icon(icon)
pygame.init()
screen = pygame.display.set_mode(monitorRes)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

pygame.display.flip()
clock.tick(60)
pygame.quit()
