from enum import Enum, auto
import numpy as np
from typing import Union, Sequence

from neural_network import NeuralNetwork

class Snake_ai:
    __MEMORY_SIZE = 6

    class Direction(Enum):
        LEFT = auto()
        RIGHT = auto()
        FORWARD = auto()

    def __init__(self):
        self.__brain = NeuralNetwork(6 + Snake_ai.__MEMORY_SIZE, 5 + Snake_ai.__MEMORY_SIZE)
        self.__memory = tuple([0] * self.__MEMORY_SIZE)

        # Perceptions
        self.__left_obstacle_color_grayscale = 0.0
        self.__left_obstacle_distance = 1

        self.__right_obstacle_color_grayscale = 0.0
        self.__right_obstacle_distance = 1

        self.__front_obstacle_color_grayscale = 0.0
        self.__front_obstacle_distance = 1

        # Actions
        self.__move_direction = Snake_ai.Direction.FORWARD
        self.__body_color_grayscale = 0.5
        self.__is_reproduce = False

    def set_left_obstacle_color_grayscale(self, grayscale_value: float):
        self.__left_obstacle_color_grayscale = grayscale_value

    def set_left_obstacle_distance(self, distance_value: int):
        self.__left_obstacle_distance = distance_value

    def set_right_obstacle_color_grayscale(self, grayscale_value: float):
        self.__right_obstacle_color_grayscale = grayscale_value

    def set_right_obstacle_distance(self, distance_value: int):
        self.__right_obstacle_distance = distance_value

    def set_front_obstacle_color_grayscale(self, grayscale_value: float):
        self.__front_obstacle_color_grayscale = grayscale_value

    def set_front_obstacle_distance(self, distance_value: int):
        self.__front_obstacle_distance = distance_value

    @property
    def move_direction(self) -> Direction:
        return self.__move_direction
    
    @property
    def body_color_grayscale(self) -> float:
        return self.__body_color_grayscale
    
    @property
    def is_reproduce(self) -> bool:
        return self.__is_reproduce

    @staticmethod
    def __softmax(x: Union[Sequence[float], np.ndarray]) -> np.ndarray:
        """
        Compute the softmax of a vector x.
    
        Parameters:
        x (sequence): Input sequence (list, tuple, or numpy array).
    
        Returns:
        numpy.ndarray: Softmax of the input.
        """
        # Convert input to a numpy array
        x = np.asarray(x)
    
        # Subtract the max value from x for numerical stability
        exp_x = np.exp(x - np.max(x))
    
        return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

    @staticmethod
    def __interpret_move_direction_output_values_with_randomness(
        move_left_value: float, move_right_value: float, move_forward_value: float) -> Direction:
        softmax_result = Snake_ai.__softmax((move_left_value, move_right_value, move_forward_value))
        random_value = np.random.uniform(0.0, 1.1)

        if random_value <= softmax_result[0]:
            return Snake_ai.Direction.LEFT
        elif random_value <= softmax_result[0] + softmax_result[1]:
            return Snake_ai.Direction.RIGHT
        else:
            return Snake_ai.Direction.FORWARD

    @staticmethod
    def __interpret_is_reproduce_output_value_with_randomness(is_reproduce_value: float) -> bool:
        random_value = np.random.uniform(0.0, 1.1)

        if random_value <= is_reproduce_value:
            return True
        else:
            return False

    def react(self):
        self.__brain.input(self.__left_obstacle_color_grayscale, 1 / self.__left_obstacle_distance,
                           self.__right_obstacle_color_grayscale, 1 / self.__right_obstacle_distance,
                           self.__front_obstacle_color_grayscale, 1 / self.__front_obstacle_distance,
                           *self.__memory)
        
        output_action_values = self.__brain.compute_output_values()

        self.__move_direction = Snake_ai.__interpret_move_direction_output_values_with_randomness(output_action_values[0:3])

        self.__body_color_grayscale = Snake_ai.__softmax((output_action_values[3], 0))[0]

        self.__is_reproduce = Snake_ai.__interpret_is_reproduce_output_value_with_randomness(output_action_values[4])

        self.__memory = output_action_values[5 : 5 + Snake_ai.__MEMORY_SIZE]