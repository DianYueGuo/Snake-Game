import math
from typing import Tuple

class __Dendrite:
    def __init__(self, input_neuron: __Neuron, weight: float):
        self.__input_neuron = input_neuron
        self.__weight = weight
    
    def get_signal(self) -> float:
        return self.__input_neuron.potential_value * self.__weight

class __Neuron:
    def __init__(self, potential_value: float, bias: float):
        self.__potential_value = potential_value
        self.__bias = bias
        self.__dendrites = []

    @classmethod
    def __logistic(x: float) -> float:
        return 1 / (1 + math.exp(-x))

    def react_to_input_signals(self) -> float:
        signal_sum = self.__bias

        for dendrite in self.__dendrites:
            signal_sum += dendrite.get_signal()

        self.__potential_value = self.__logistic(signal_sum)

        return self.__potential_value
    
    @potential_value.setter
    def potential_value(self, potential_value: float):
        self.potential_value = potential_value

    @property
    def potential_value(self) -> float:
        return self.__potential_value

class __NeuralNetwork:
    def __init__(self, n_input_neurons, n_output_neurons):
        self.__n_input_neurons = n_input_neurons
        self.__n_output_neurons = n_output_neurons

        self.__input_neurons = [__Neuron(0, 0) for _ in range(self.__n_input_neurons)]
        self.__output_neurons = [__Neuron(0, 0) for _ in range(self.__n_output_neurons)]

        self.__hidden_neurons = []

    def input(self, *input_values: float):
        if len(input_values) != self.__n_input_neurons:
            raise ValueError(f"Expected {self.__n_input_neurons} input values, but got {len(input_values)}")
        
        for i, input_value in enumerate(input_values):
            self.__input_neurons[i].potential_value = input_value

    def get_output_values(self) -> Tuple[float, ...]:
        for node in self.__hidden_neurons:
            node.react_to_input_signals()

        return tuple([node.react_to_input_signals() for node in self.__output_neurons])