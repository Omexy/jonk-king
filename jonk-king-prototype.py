import pygame, sys, ctypes, time #Relevant modules imported
resolution = [1280, 720]
colour = (255, 100, 98)
surfaceColour = (167, 255, 100)

# Object classes
class Sprite(pygame.sprite.Sprite): # Player/Sprite Class
    def __init__(self, colour, width, height):
        super().__init__()

        self.image = pygame.Surface(resolution)
        self.image.fill(surfaceColour)
        self.image.set_colorkey(colour)
        pygame.draw.rect(self.image, colour, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        
    def gravity(self):
        self.rect.y += 2.5

    def jump(self):
        self.rect.y -= 50
        
    def onBottom(self):
        if self.rect.bottom >= 720:
            return True
        else:
            return False

pygame.display.set_caption('Jonk King') #Window title
icon = pygame.image.load('jonk-king.ico') #Loads icon into pygame
pygame.display.set_icon(icon) #Window icon
pygame.init()
screen = pygame.display.set_mode(resolution) #Sets resolution to 1280x720
all_sprites_list = pygame.sprite.Group()
playerCar = Sprite((255, 0, 0), 175, 175)
playerCar.rect.x = 640
playerCar.rect.y = 360
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Quits game when X is clicked
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #Quits game when ESC is pressed
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerCar.jump()
    # Defines a list of boolean values to see if each key is pressed
    keys = pygame.key.get_pressed()
    # Checks if the keys are pressed to move left/right
    if keys[pygame.K_a]:
        playerCar.moveLeft(10)
    if keys[pygame.K_d]:
        playerCar.moveRight(10)
    # Checks if no key is pressed and if the player is at the bottom of the screen to apply gravity
    if playerCar.onBottom() == False:
        playerCar.gravity()

#ADD CODE TO FRAMEWORK HERE

    all_sprites_list.update()
    screen.fill(surfaceColour)
    all_sprites_list.draw(screen)
    pygame.display.flip() #Allows for images to be added
    clock.tick(60) #Sets FPS to 60
    
pygame.quit()
