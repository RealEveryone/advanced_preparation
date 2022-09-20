from abc import ABC, abstractmethod


class BaseDecoration(ABC):
    def __init__(self, comfort, price):
        self.comfort = comfort
        self.price = price

    @property
    @abstractmethod
    def type(self):
        pass

