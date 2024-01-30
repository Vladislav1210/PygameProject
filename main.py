import pygame


if __name__ == '__main__':

    pygame.init()
    s = pygame.image.load('sprites/t34.png')
    size = width, height = 1200, 820
    x, y = 600, 400
    screen = pygame.display.set_mode(size)
    pygame.draw.line(screen, (255, 0, 0), (200, 0), (200, 820), width=1)
    pygame.draw.line(screen, (255, 0, 0), (1000, 0), (1000, 820), width=1)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                y -= 1
            screen.blit(s, (x, y))
        pygame.display.update()
    screen.fill((0, 0, 0))
    pygame.quit()
