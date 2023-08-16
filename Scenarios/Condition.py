from abc import ABC, abstractmethod

class Condition(ABC):

    def __init__(self, random_generation: bool) -> None:
        self.random_gen = random_generation
        
    @abstractmethod
    def load(self):
        pass
    pass