import pygame

# GLOBAL VARIABLES
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 1280
HEIGHT = 720

# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
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

# Initialising
pygame.init()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

all_sprites_list = pygame.sprite.Group()
playerCar = Sprite((255, 0, 0), 175, 175)
playerCar.rect.x = 640
playerCar.rect.y = 360
all_sprites_list.add(playerCar)

running = True
clock = pygame.time.Clock()

while running:
    # Checks if x pressed to close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # Checks if the event is a key press and if it is "w" to jump once
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

    # Updates screen
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
