import pygame, sys, random

class Player(pygame.sprite.Sprite):
    def __int__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(200, 300))


def display_score():
    current_time = pygame.time.get_ticks() // 1000 - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return obstacle_list


def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True


def player_animation():
    # play walking animation if player is on floor
    # display the jump surface when player is not on floor
    global player_surface, player_index

    if player_rect.bottom < 300:
        # show jump
        player_surface = player_jump
    else:
        player_index += 0.1
        # if player_index >= len(player_walk): player_index = 0
        player_surface = player_walk[int(player_index) % 2]
        # show walk


pygame.init()
# width - left to right
# height - up to down
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

start_time = 0
score = 0

# font type, font size
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

game_active = False

sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

score_surface = test_font.render('My Game', False, 'Blue')
score_rect = score_surface.get_rect(center=(400, 50))

player = pygame.sprite.GroupSingle()
player.add(Player())

player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
##player_stand = pygame.transform.scale(player_stand, (200, 400))
player_stand = pygame.transform.scale2x(player_stand)
##player_stand = pygame.transform.rotozoom(player_stand, 0, 2)

player_stand_rect = player_stand.get_rect(center=(400, 200))

# obstacles
snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
# snail_rect = snail_surface.get_rect(bottomright = (600, 300))
snail_frame_index = 0

snail_surface = snail_frames[snail_frame_index]

fly_frame_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

obstacle_rect_list = []

player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()

player_surface = player_walk[player_index]
# left top width height for pygame.Rect
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

game_name = test_font.render('Pixel Runner', False, (111, 196, 196))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = test_font.render('Press space to run', False, (111, 196, 196))
game_message_rect = game_message.get_rect(center=(400, 335))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    # draw all our elements
    # update everything
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                player_gravity = -20
        ##        if event.type == pygame.MOUSEBUTTONDOWN:
        ##            mouse_pos = pygame.mouse.get_pos()
        ##            if player_rect.collidepoint(mouse_pos):
        ##                player_gravity = -20
        ##            if player_rect.collidepoint(event.pos):
        ##                print('Collision')
        # button is pressed
        if event.type == pygame.KEYDOWN:
            print('key down')
            if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                print('Jump')
                player_gravity = -20
        # button is released
        if event.type == pygame.KEYUP:
            print('key up')

        if game_active:
            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]

            if event.type == obstacle_timer:
                snail_rect = snail_surface.get_rect(bottomright=(random.randint(900, 1100), 300))
                fly_rect = fly_surface.get_rect(bottomright=(random.randint(900, 1100), 210))
                if random.randint(0, 2):
                    obstacle_rect_list.append(snail_rect)
                else:
                    obstacle_rect_list.append(fly_rect)
    # block image transfer; putting a surface onto another surface
    # (0,0) is origin point. larger y = lower; larger x = further right
    # (width, height)
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        ##        pygame.draw.rect(screen, '#c0e8ec', score_rect)
        ##        pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        score = display_score()

        # pygame.draw.line(screen, '#c0e8ec', (0,0), (800, 400))

        ##        screen.blit(score_surface, score_rect)
        # player_rect.top += 1
        ##        snail_rect.x -= 5
        ##        if snail_rect.x < -100:
        ##            snail_rect.x = 800
        ##
        ##        screen.blit(snail_surface, snail_rect)

        # Player
        player_gravity += 1
        screen.blit(player_surface, player_rect)
        player_rect.y += player_gravity

        # obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # will potential cause multiple true cases. Find a way to only check 1 coliison
        ##        if snail_rect.colliderect(player_rect):
        ####            pygame.quit()
        ####            sys.exit()
        ##            game_active = False

        ##    mouse_pos = pygame.mouse.get_pos()
        ##    if player_rect.collidepoint(mouse_pos):
        ##        print('collision')

        mouse_pos = pygame.mouse.get_pos()
        if player_rect.collidepoint(mouse_pos):
            print(pygame.mouse.get_pressed())

        ##    keys = pygame.key.get_pressed()
        ##    if keys[pygame.K_SPACE]:
        ##        print('Jump')
        player_animation()
        if player_rect.bottom > 300:
            player_rect.bottom = 300

        game_active = collisions(player_rect, obstacle_rect_list)
    ##        print(snail_rect, player_rect)
    else:
        screen.fill((94, 129, 162))
        keys = pygame.key.get_pressed()
        screen.blit(game_name, game_name_rect)

        score_message = test_font.render(f'Your Score: {score}', False, (11, 196, 196))
        score_rect = score_message.get_rect(center=(400, 330))

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_rect)

        player.draw(screen)
        screen.blit(player_stand, player_stand_rect)

        if keys[pygame.K_SPACE]:
            game_active = True
            # snail_rect.x = 800
            player_rect.midbottom = (80, 300)
            player_gravity = 0
            obstacle_rect_list.clear()
            start_time = pygame.time.get_ticks() // 1000

    pygame.display.update()
    clock.tick(60)
