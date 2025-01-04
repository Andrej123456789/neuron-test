# AUTHOR Andrej Bartulin
# PROJECT: neuron-test
# LICENSE: Public Domain
# DESCRIPTION: Simple neural network test
# CREDITS: https://www.youtube.com/watch?v=a9NprGqBr54&t=487s&ab_channel=TechAltar

from dataclasses import dataclass, field
from typing import List

import os
import sys

@dataclass
class Neuron:
    value: float
    connected_to: List['Neuron'] = field(default_factory=list)

@dataclass
class Layer:
    neurons: List['Neuron'] = field(default_factory=list)

def initialize_network(content) -> Layer:
    starting_layer = Layer()

    for c in content:
        starting_layer.neurons.append(Neuron(value=float(c)))

    return starting_layer

def main(content: list):
    starting_layer = Layer()
    last_layer = Layer()

    last_layer.neurons.append(Neuron(value=0.0))
    last_layer.neurons.append(Neuron(value=0.0))

    for c in content:
        neuron = Neuron(value=float(c), connected_to=[
            last_layer.neurons[0],
            last_layer.neurons[1],
        ])

        starting_layer.neurons.append(neuron)
        
    # ---------------------------------

    for i in range(len(starting_layer.neurons)):
        if i == 0 or i == 3:
            last_layer.neurons[0].value += starting_layer.neurons[i].value * 0.5
            last_layer.neurons[1].value += starting_layer.neurons[i].value * -0.5

        if i == 1 or i == 2:
            last_layer.neurons[0].value += starting_layer.neurons[i].value * -0.5
            last_layer.neurons[1].value += starting_layer.neurons[i].value * 0.5

    # ---------------------------------

    if last_layer.neurons[0].value == 1:
        print("Left white diagonal")

    elif last_layer.neurons[1].value == 1:
        print("Right white diagonal")

    else:
        print("No diagonal")

    print(f"Neuron 0: {last_layer.neurons[0].value}")
    print(f"Neuron 1: {last_layer.neurons[1].value}")

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
