from math import floor

from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, 'Power', floor(0.25 * capacity), floor(1.75 * memory))

