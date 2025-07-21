import pygame

clock = pygame.time.Clock()

pygame.init()
running = True
screen = pygame.display.set_mode((1640, 640))


player = pygame.Rect((800, 320, 40, 40))


while running:

    clock.tick(144)
    screen.fill((0, 0, 0))
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