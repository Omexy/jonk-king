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
        
        # Jumping and gravity variables
        self.vertical_velocity = 0
        self.gravity_coefficient = 0.5
        self.jump_power = -10
        self.is_jumping = False
        self.max_jump_power = -20
        self.a = 0  # Jump charge variable
        self.is_charging = False

    def moveRight(self, pixels):
        if not self.is_jumping:
            self.rect.x += pixels

    def moveLeft(self, pixels):
        if not self.is_jumping:
            self.rect.x -= pixels

    def apply_gravity(self):
        self.vertical_velocity += self.gravity_coefficient
        self.rect.y += self.vertical_velocity
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.vertical_velocity = 0
            self.is_jumping = False
            self.a = 0  # Reset the jump charge when landing

    def jump(self, charging=False):
        if charging:
            if not self.is_jumping:
                self.is_charging = True
                self.a += 1  # Increase jump charge while space is held
            if self.a >= 10:  # Trigger the jump if charge reaches 10
                self._do_jump()
        else:
            if self.is_charging:  # Trigger the jump if space is released and it was charging
                self._do_jump()

    def _do_jump(self):
        self.is_jumping = True
        self.is_charging = False
        self.vertical_velocity = self.jump_power - (self.a / 2)  # Adjust jump power based on charge
        self.a = 0  # Reset the jump charge

    def update(self):
        self.apply_gravity()
        
    def onBottom(self):
        return self.rect.bottom >= HEIGHT

pygame.init()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

all_sprites_list = pygame.sprite.Group()
playerCar = Sprite((255, 0, 0), 50, 50)
playerCar.rect.x = 640
playerCar.rect.y = 670
all_sprites_list.add(playerCar)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if not playerCar.is_jumping:
        if keys[pygame.K_a]:
            playerCar.moveLeft(10)
        if keys[pygame.K_d]:
            playerCar.moveRight(10)
    if keys[pygame.K_SPACE]:
        playerCar.jump(charging=True)
    elif playerCar.is_charging:  # Check if space is released and it was charging
        playerCar.jump(charging=False)

    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
