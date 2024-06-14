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
        a -= 0.1

    def jump(self):
        a = 0.1
        global a
        while True:
            if keys[pygame.K_w]:
                a += 0.05
                print(a)
                if a <= 10:
                    break
                for event in pygame.event.get():
                    if event.type == pygame.KEYUP:
                        break
            
                
        
    def onBottom(self):
        if self.rect.bottom >= 720:
            return True
        else:
            return False
        
pygame.init()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

all_sprites_list = pygame.sprite.Group()
playerCar = Sprite((255, 0, 0), 362, 351)
playerCar.rect.x = 640
playerCar.rect.y = 360
all_sprites_list.add(playerCar)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        playerCar.moveLeft(10)
    if keys[pygame.K_d]:
        playerCar.moveRight(10)
    if keys[pygame.K_w]:
        playerCar.jump()
    if (not(True in keys)) and (playerCar.onBottom() == False):
        playerCar.gravity()
        
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)   
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
