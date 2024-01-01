from all import *
import pygame
pygame.init()

width,height = 1280,720
screen = pygame.display.set_mode((width,height))
running = True
pygame.mouse.set_visible(True)
clock = pygame.time.Clock()
t = trail2(9,(0,100,100),5)
t2 = trail2(15,(0,150,150),10)
delay = 5
tick = 0
while running:
    clock.tick(240)
    tick += 1
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if tick % delay == 0 :
        t.newangle()  
        t2.newangle()
        tick = 0 

    t2.drawtrail(screen)
    t.drawtrail(screen)
    
    pygame.display.flip()