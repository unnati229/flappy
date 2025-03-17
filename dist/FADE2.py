import pygame
pygame.init()

WHITE = (255, 255, 255,50)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255, 70)  # This color contains an extra integer. It's the alpha value.
PURPLE = (255, 0, 255)

screen = pygame.display.set_mode((500, 500))
screen.fill(BLACK)  # Make the background white. Remember that the screen is a Surface!
clock = pygame.time.Clock()


pygame.draw.circle(screen, BLUE, (200,200), 50)
pygame.display.update()


run =True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            quit()

pygame.quit()
