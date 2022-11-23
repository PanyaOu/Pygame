import pygame, sys, time
#from debug import debug

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

test_rect = pygame.Rect(0, 310, 100, 100)
test_rect_pos = test_rect.x
test_speed = 200

previous_time = time.time()
while True:
    #method 1
    #dt = clock.tick(60)/1000

    #method 2
    dt = time.time() - previous_time
    previous_time = time.time()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('gold')
    test_rect_pos += test_speed *dt
    test_rect.x = round(test_rect_pos)
    
    pygame.draw.rect(screen, 'silver', test_rect)

    pygame.display.update()
