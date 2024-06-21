import pygame
import sys

def convert_number_into_grayscale_color(number: float):
    NUMBER_UPPER_BOUND = 1.0
    NUMBER_LOWER_BOUND = 0.0

    if not (NUMBER_LOWER_BOUND <= number <= NUMBER_UPPER_BOUND):
        raise ValueError(f"Value {number} is out of bounds. It should be between {NUMBER_LOWER_BOUND} and {NUMBER_UPPER_BOUND}.")

    grayscale_value = (number - NUMBER_LOWER_BOUND) / (NUMBER_UPPER_BOUND - NUMBER_LOWER_BOUND)
    color_value = int(255 * grayscale_value)

    return pygame.Color(color_value, color_value, color_value)

def draw(window):
    pygame.draw.rect(window, convert_number_into_grayscale_color(0.5), (50, 50, 200, 100))

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

        # Draw the window
        draw(window)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate to 60 frames per second
        clock.tick(60)

    # Clean up and close the window
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()