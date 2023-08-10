from abc import ABC, abstractmethod

class Condition(ABC):

    def __init__(self, requires_load_handler: int) -> None:
        self.requires_load_handler = requires_load_handler

    @abstractmethod
    def load(self):
        pass
    pass