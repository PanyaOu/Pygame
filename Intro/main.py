import pygame
import sys

pygame.init()
height = 1000
width = 500
dimension = (height, width)
screen = pygame.display.set_mode(dimension)

clock = pygame.time.Clock()

w = 100
h = 200
#need to display and update

#inputs : width, height
test_surface = pygame.Surface((w, h))

#inputs : x, y, width, height
test_rectangle = pygame.Rect(100, 200, 100, 100)

pygame.display.set_caption('Panya\'s Runner')

#increasing x - movement to right
x_pos = 500
#increase y - movement downwards
y_pos = 250

x = 200
y = 250
test_rect = test_surface.get_rect(center = (x, y))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #fill the screen with a specific color
    #screen.fill(pygame.Color('gold'))
    screen.fill((175, 215, 70))

    #fills test_surface with blue
    test_surface.fill(pygame.Color('blue'))

    #x position changes
    x_pos += 1
    y_pos += 1

    #inputs : Surface, color, rectange
    pygame.draw.rect(screen, pygame.Color('red'), test_rectangle)
    screen.blit(test_surface, test_rect)
    pygame.display.update()
    # setting max fps to 60
    clock.tick(60)
    
