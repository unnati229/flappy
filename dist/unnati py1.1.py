import pygame
# Create a surface with per-pixel alpha.
surface = pygame.Surface((640, 480), pygame.SRCALPHA)
# Draw a rectangle on the surface.
pygame.draw.rect(surface, (255, 0, 0), (100, 100, 100, 100))
# Display the surface.
pygame.display.set_mode((640, 480))
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
