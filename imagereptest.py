import pygame

# pygame setup
pygame.init()
width = 1280; vert = 720
screen = pygame.display.set_mode((width, vert))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame

    jonk = pygame.image.load("jonktest.png")
    jonkrez = [184,346]
    pygame.Surface.set_colorkey(jonk, [255,255,255])
    screen.blit(jonk, (width/2-jonkrez[0]/2,vert/2-jonkrez[1]/2))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
