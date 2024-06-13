import pygame, sys, ctypes, time #Relevant modules imported
resolution = [1280, 720]

pygame.display.set_caption('Jonk King') #Window title
icon = pygame.image.load('jonk-king.ico') #Loads icon into pygame
pygame.display.set_icon(icon) #Window icon
pygame.init()
screen = pygame.display.set_mode(resolution) #Sets resolution to 1280x720
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Quits game when X is clicked
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #Quits game when ESC is pressed
                running = False

#ADD CODE TO FRAMEWORK HERE

pygame.display.flip() #Allows for images to be added
clock.tick(60) #Sets FPS to 60
pygame.quit()
