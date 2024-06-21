import pygame
import sys

def main():
    # Initialize Pygame
    pygame.init()

    # Set up display
    window_size = (800, 600)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption('My Pygame Window')

    # Set up the clock for managing the frame rate
    clock = pygame.time.Clock()

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        # Fill the window with a color (RGB)
        window.fill((0, 0, 0))  # Black background

        # Update the display
        pygame.display.flip()

        # Cap the frame rate to 60 frames per second
        clock.tick(60)

    # Clean up and close the window
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()