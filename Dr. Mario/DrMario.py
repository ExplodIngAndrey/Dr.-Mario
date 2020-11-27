import pygame

# Initialize Pygame
pygame.init()

# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('Background.png')

# Title and Icon
pygame.display.set_caption('Dr. Mario')
icon = pygame.image.load('Logo.png')
pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    screen.blit(background, (0, 0))
    # Check for Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()  # Updates Screen