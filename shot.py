import circleshape
import pygame
import constants

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, constants.ASTEROID_DRAW_LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt