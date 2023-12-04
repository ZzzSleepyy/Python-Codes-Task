import pygame
import sys
import math


pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")


clock = pygame.time.Clock()


class Player:
    def __init__(self, pos):
        self.pos = pos
        self.angle = 0

    def draw(self):
        rotated_player = pygame.transform.rotate(player_surface, -self.angle)
        rotated_rect = rotated_player.get_rect(center=self.pos)
        screen.blit(rotated_player, rotated_rect.topleft)


class Shot:
    def __init__(self, x, y, angle):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.angle = angle

    def move(self):
        speed = 10
        self.rect.x += speed * math.cos(math.radians(self.angle))
        self.rect.y += speed * math.sin(math.radians(self.angle))

    def draw(self):
        pygame.draw.rect(screen, "black", self.rect)

# Load player image
player_surface = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(player_surface, "red", (10, 10), 10)


player = Player((400, 300))
shots = []


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("white")

    x, y = pygame.mouse.get_pos()


    dx = x - player.pos[0]
    dy = y - player.pos[1]
    player.angle = math.degrees(math.atan2(dy, dx))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.pos = (player.pos[0], player.pos[1] - 300 * dt)
    if keys[pygame.K_s]:
        player.pos = (player.pos[0], player.pos[1] + 300 * dt)
    if keys[pygame.K_a]:
        player.pos = (player.pos[0] - 300 * dt, player.pos[1])
    if keys[pygame.K_d]:
        player.pos = (player.pos[0] + 300 * dt, player.pos[1])

    if pygame.mouse.get_pressed()[0]:

        offset_x = 20 * math.cos(math.radians(player.angle))
        offset_y = 20 * math.sin(math.radians(player.angle))
        

        shots.append(Shot(player.pos[0] + offset_x, player.pos[1] + offset_y, player.angle))

 
    player.draw()

 
    for shot in shots:
        shot.move()
        shot.draw()


    shots = [shot for shot in shots if 0 < shot.rect.y < 600]

    pygame.display.flip()

    dt = clock.tick(60) / 1000  
