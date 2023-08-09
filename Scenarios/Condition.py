from abc import ABC, abstractmethod

class Condition(ABC):

    @abstractmethod
    def load(self):
        pass
    pass