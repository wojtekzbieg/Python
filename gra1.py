import pygame

clock = pygame.time.Clock()

pygame.init()
screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
running = True

player = pygame.Rect((800, 320, 40, 40))

background = (0, 0, 0)
snake_colour = (255, 0, 0)
cell_size = 10

snake_position = [[int(screen_width / 2), int(screen_height / 2)]]

def draw_screen():
    screen.fill(background)

while running:

    clock.tick(144)

    draw_screen()

    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player.move_ip(0, -1)
    elif key[pygame.K_a] :
        player.move_ip(-1, 0)
    elif key[pygame.K_s]:
        player.move_ip(0, 1)
    elif key[pygame.K_d]:
        player.move_ip(1, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()




pygame.quit()