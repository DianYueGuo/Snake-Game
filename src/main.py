import pygame
import sys
import numpy as np

def __convert_number_into_grayscale_color(number: float):
    NUMBER_UPPER_BOUND = 1.0
    NUMBER_LOWER_BOUND = 0.0

    if not (NUMBER_LOWER_BOUND <= number <= NUMBER_UPPER_BOUND):
        raise ValueError(f"Value {number} is out of bounds. It should be between {NUMBER_LOWER_BOUND} and {NUMBER_UPPER_BOUND}.")

    grayscale_value = (number - NUMBER_LOWER_BOUND) / (NUMBER_UPPER_BOUND - NUMBER_LOWER_BOUND)
    color_value = int(255 * grayscale_value)

    return pygame.Color(color_value, color_value, color_value)

def __draw(window, game_screen: np.ndarray):
    LINE_WIDTH_TO_BLOCK_WIDTH_RATIO = 0.05
    
    # Check if game_screen is a NumPy array
    if not isinstance(game_screen, np.ndarray):
        raise TypeError("game_screen must be a NumPy array")

    # Check if game_screen has two dimensions
    if game_screen.ndim != 2:
        raise ValueError("game_screen must have two dimensions")
    
    # Check if game_screen has non-zero dimensions
    if game_screen.shape[0] == 0 or game_screen.shape[1] == 0:
        raise ValueError("game_screen must have non-zero dimensions")

    block_width = min(window.get_width() / (LINE_WIDTH_TO_BLOCK_WIDTH_RATIO + (1 + LINE_WIDTH_TO_BLOCK_WIDTH_RATIO) * game_screen.shape[0]),
                    window.get_height() / (LINE_WIDTH_TO_BLOCK_WIDTH_RATIO + (1 + LINE_WIDTH_TO_BLOCK_WIDTH_RATIO) * game_screen.shape[1]))

    start_printing_point_x = window.get_width() / 2 - block_width * (LINE_WIDTH_TO_BLOCK_WIDTH_RATIO + (1 + LINE_WIDTH_TO_BLOCK_WIDTH_RATIO) * game_screen.shape[0]) / 2
    start_printing_point_y = window.get_height() / 2 - block_width * (LINE_WIDTH_TO_BLOCK_WIDTH_RATIO + (1 + LINE_WIDTH_TO_BLOCK_WIDTH_RATIO) * game_screen.shape[1]) / 2

    for i, row in enumerate(game_screen):
        for j, number in enumerate(row):
            pygame.draw.rect(window, __convert_number_into_grayscale_color(number), 
                             (start_printing_point_x + block_width * LINE_WIDTH_TO_BLOCK_WIDTH_RATIO + block_width * (1 + LINE_WIDTH_TO_BLOCK_WIDTH_RATIO) * i,
                              start_printing_point_y + block_width * LINE_WIDTH_TO_BLOCK_WIDTH_RATIO + block_width * (1 + LINE_WIDTH_TO_BLOCK_WIDTH_RATIO) * j,
                              block_width, block_width))

def __main():
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
        __draw(window, np.ones((2, 5)))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate to 60 frames per second
        clock.tick(60)

    # Clean up and close the window
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    __main()