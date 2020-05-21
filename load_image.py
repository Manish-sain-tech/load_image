import pygame
pygame.init()

win =pygame.display.set_mode((400,600))
pygame.display.set_caption("space_fighter")

bg=pygame.image.load('background.jpeg')
bullet=pygame.image.load('bullet.png')
space_ship=pygame.image.load('spaceship.png')
x=150
y=500

def redraw():
    
            win.blit(bg,(0,0))
            win.blit(space_ship,(x,y))
                            
            win.blit(space_ship,(x,y))
            pygame.display.update()
redraw()
