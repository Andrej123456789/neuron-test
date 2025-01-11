# AUTHOR Andrej Bartulin
# PROJECT: neuron-test
# LICENSE: Public Domain
# DESCRIPTION: Simple neural network test
# CREDITS: https://www.youtube.com/watch?v=a9NprGqBr54&t=487s&ab_channel=TechAltar

from dataclasses import dataclass, field
from typing import List

import os
import sys

LAYERS_IN_NETWORK: int = 2

@dataclass
class Neuron:
    value: float
    weights: List['float'] = field(default_factory=list)

@dataclass
class Layer:
    neurons: List['Neuron'] = field(default_factory=list)

def initialize_layer(size: int) -> Layer:
    layer = Layer()

    for i in range(size):
        neuron = Neuron(value=0.0)
        layer.neurons.append(neuron)

    return layer

def assign_starting_layer(layer: Layer, content: str) -> Layer:
    for i in range(len(layer.neurons)):
        weight1 = 0.5 if (i == 0 or i == 3) else -0.5
        weight2 = -0.5 if (i == 0 or i == 3) else 0.5

        layer.neurons[i].value = float(content[i])
        layer.neurons[i].weights=[weight1, weight2]

    return layer

def multiply_layer(first_layer: Layer, second_layer: Layer) -> Layer:
    for i in range(len(first_layer.neurons)):
        for j in range(len(second_layer.neurons)):
            second_layer.neurons[j].value += first_layer.neurons[i].value * first_layer.neurons[i].weights[j]

    return second_layer

def main(content: list):
    network = []

    starting_layer = initialize_layer(4)
    last_layer = initialize_layer(2)

    network.append(starting_layer)
    network.append(last_layer)

    starting_layer = assign_starting_layer(starting_layer, content)
    
    for i in range(LAYERS_IN_NETWORK - 1): # do not multiply last layer
        network[i + 1] = multiply_layer(network[i], network[i + 1])

    if network[LAYERS_IN_NETWORK - 1].neurons[0].value == 1:
        print("Left white diagonal")

    elif network[LAYERS_IN_NETWORK - 1].neurons[1].value == 1:
        print("Right white diagonal")

    else:
        print("No diagonal")

    print(f"Neuron 0: {network[LAYERS_IN_NETWORK - 1].neurons[0].value}")
    print(f"Neuron 1: {network[LAYERS_IN_NETWORK - 1].neurons[1].value}")

if __name__ == "__main__":
    path: str = None
    content: list = []

    print("--------------------")
    print("Neuron network text")
    print("--------------------")

    if len(sys.argv) < 2:
        path = input("Enter a path to the file: ")

    else:
        path = sys.argv[1]

    if not os.path.isfile(path):
        print("File not found!")
        print("Exiting...")

        exit(0)

    with open(path) as f:
        while True: 
            c = f.read(1)
            if not c:
                break

            if c == ' ' or c == '\n':
                continue

            content.append(c)

    main(content)
