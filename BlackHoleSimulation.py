import pygame
import numpy
import math

from pygame import camera

pygame.init()
display = pygame.display.set_mode((800,800))
pygame.display.set_caption("BlackHole")
clock = pygame.time.Clock()
dt = 1
G = 1
M = 1000
c = 10
r_s = 2 * G * M / (c**2)

x = 0
y = -200

vx = 2.0
vy = 0.0


trail = []
captured = False
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    display.fill((0,0,0))
    r = math.sqrt(x**2 + y**2)
    if r <= r_s:
        captured = True

    if not captured:
        L = x * vy - y * vx
        a_mag = -(G * M) / (r ** 2) - (3 * G * M * L ** 2) / ((c ** 2) * (r ** 4))
        ax = a_mag * (x / r)
        ay = a_mag * (y / r)
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        screen_x = 400 + int(x)
        screen_y = 400 - int (y)
        if len(trail) >= 2:
            pygame.draw.lines(display, (100, 100, 255), False, trail, 2)
        trail.append((screen_x, screen_y))

        pygame.draw.circle(display,(255,194,97), (400,400), int(r_s))
        pygame.draw.circle(display, (255, 255, 255), (screen_x, screen_y), 20)
    pygame.display.update()
    clock.tick(60)

pygame.quit()