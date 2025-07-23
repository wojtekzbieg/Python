import pygame
from pygame.locals import *
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
over_rect = Rect(screen_width // 2 - 80, screen_height // 2 - 60, 160, 50)
again_rect = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)
clicked = False

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

def draw_game_over():
    over_text = "Game Over!"
    over_img = font.render(over_text, True, (0, 0, 255))
    pygame.draw.rect(screen, (255, 0, 0), over_rect)
    screen.blit(over_img, (screen_width // 2 - 80, screen_height // 2 - 50))

    again_text = 'Play Again?'
    again_img = font.render(again_text, True, (0, 0, 255))
    pygame.draw.rect(screen, (255, 0, 0), again_rect)
    screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 10))


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

            snake_pos = snake_pos[-1:] + snake_pos[:-1]

            if direction == 1:
                snake_pos[0][0] = snake_pos[1][0]
                snake_pos[0][1] = snake_pos[1][1] - cell_size
            if direction == 3:
                snake_pos[0][0] = snake_pos[1][0]
                snake_pos[0][1] = snake_pos[1][1] + cell_size
            if direction == 2:
                snake_pos[0][1] = snake_pos[1][1]
                snake_pos[0][0] = snake_pos[1][0] + cell_size
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

    if snake_pos[0][0] < 0 or snake_pos[0][0] >= screen_width or snake_pos[0][1] < 0 or snake_pos[0][1] >= screen_height or snake_pos[0] in snake_pos[1:]:
        game_over = True

    if game_over is True:
        draw_game_over()
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                game_over = False
                update_snake = 0
                food = [0, 0]
                new_food = True
                snake_pos = [[int(screen_width / 2), int(screen_height / 2)]]
                snake_pos.append([snake_pos[0][0], snake_pos[0][1] + cell_size])
                snake_pos.append([snake_pos[0][0], snake_pos[0][1] + cell_size * 2])
                snake_pos.append([snake_pos[0][0], snake_pos[0][1] + cell_size * 3])
                direction = 1
                score = 0
            elif over_rect.collidepoint(pos):
                running = False

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