import pygame
import random

# clock = pygame.time.Clock()

pygame.init()
screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake')
update_snake = 0
running = True

background = (0, 0, 0)
cell_size = 10
food = []
new_food = True
score = 0
font = pygame.font.SysFont(None, 40)
game_over = False


snake_pos = [[int(screen_width / 2), int(screen_height / 2)]]
snake_pos.append([snake_pos[0][0], snake_pos[0][1]+cell_size])
snake_pos.append([snake_pos[0][0], snake_pos[0][1]+cell_size*2])
snake_pos.append([snake_pos[0][0], snake_pos[0][1]+cell_size*3])
direction = 1

def draw_screen():
    screen.fill(background)

def draw_score():
    score_txt = "Score: " + str(score)
    score_img = font.render(score_txt, True, (0, 0, 255), )
    screen.blit(score_img, (10, 10))

while running:

    # clock.tick(144)

    draw_screen()
    draw_score()

    key = pygame.key.get_pressed()
    if key[pygame.K_w] and direction != 3:
        direction = 1
    elif key[pygame.K_a] and direction != 2 :
        direction = 4
    elif key[pygame.K_s] and direction != 1:
        direction = 3
    elif key[pygame.K_d] and direction != 4:
        direction = 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_over is False:
        if update_snake > 90:
            update_snake = 0
            # first shift the positions of each snake piece back.
            snake_pos = snake_pos[-1:] + snake_pos[:-1]
            # now update the position of the head based on direction
            # heading up
            if direction == 1:
                snake_pos[0][0] = snake_pos[1][0]
                snake_pos[0][1] = snake_pos[1][1] - cell_size
            # heading down
            if direction == 3:
                snake_pos[0][0] = snake_pos[1][0]
                snake_pos[0][1] = snake_pos[1][1] + cell_size
            # heading right
            if direction == 2:
                snake_pos[0][1] = snake_pos[1][1]
                snake_pos[0][0] = snake_pos[1][0] + cell_size
            # heading left
            if direction == 4:
                snake_pos[0][1] = snake_pos[1][1]
                snake_pos[0][0] = snake_pos[1][0] - cell_size

    if new_food is True:
        food = [random.randint(1, int(screen_width/10-1))*10, random.randint(1, int(screen_height/10-1))*10]
        new_food = False

    if snake_pos[0] == food:
        new_food = True
        snake_pos.append([snake_pos[-1][0], snake_pos[-1][1]])
        score += 1
        print(score)

    if snake_pos[0][0] < 0 or snake_pos[0][0] >= screen_width or snake_pos[0][1] < 0 or snake_pos[0][1] >= screen_height or snake_pos[0] in snake_pos[1:]:
        game_over = True

    head = 1
    for x in snake_pos:
        if head == 0:
            pygame.draw.rect(screen, (255,255,0), (x[0], x[1], cell_size, cell_size))
        if head == 1:
            pygame.draw.rect(screen, (255, 0, 0), (x[0], x[1], cell_size, cell_size))
            head = 0

    pygame.draw.rect(screen, (0, 255, 0), (food[0], food[1], cell_size, cell_size))


    pygame.display.update()
    update_snake += 1




pygame.quit()