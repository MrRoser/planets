import pygame, sys

# Initialize Pygame
pygame.init()

# Global Constants
width = 800
height = 600
center = (width // 2, height // 2)

# Set up the window
window = pygame.display.set_mode((800, 600))


# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.circle(window, (255, 204, 0), center, 20)
    pygame.draw.circle(window, (102, 255, 51), (100,100), 10)

    # Update the window
    pygame.display.update()